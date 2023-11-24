from celery import shared_task
import time
from datetime import datetime

from .models import Email
from B_User.models import User
from C_Client.models import Client


import imaplib
import email as email_parser


@shared_task
def retrivingEmails():
    # Getting User Credentials
    user = User.objects.first()
    server = User.objects.first().imap_server
    password = User.objects.first().imap_password
    email = User.objects.first().imap_email
    port = User.objects.first().imap_port

    # connection to the server
    imap = imaplib.IMAP4_SSL(server, port)
    imap.login(email, password)
    print("Connection to Inbox successful")
    imap.select("Inbox")

    # Search Criteria
    _, msgnums = imap.search(None, "ALL")

    # Printing the number of E-Mails
    num_emails = len(msgnums[0].split())
    print(f"Number of emails in the inbox: {num_emails}")

    for mgsnum in msgnums[0].split():

        _, data = imap.fetch(mgsnum, "(RFC822)")
        print("Fetching email successful")

        message = email_parser.message_from_bytes(data[0][1])

        message_text = ""

        for part in message.walk():
            if part.get_content_type() == "text/plain":
                message_text += part.as_string()

        # Convert Email date to python date
        received_date_string = message.get('Date')
        try:
            date_without_timezone = received_date_string[:-4]
            received_date = datetime.strptime(date_without_timezone, "%a, %d %b %Y %H:%M:%S")
            print(f"Conversion worked for email {message.get('Subject')}")
            formatted_date = received_date.strftime('%Y-%m-%d %H:%M')
            print("test")
        
        except ValueError:
            print("Date parsing failed. Format mismatch or invalid date string.")
        
        # Striping everything but the E-Mail from sender
        from_sender = message.get('From').split('<')
        from_sender = from_sender[1][:-1]

        # Looking if the email already exists in database
        duplicate_email_check = Email.objects.filter(
        sender=from_sender,
        subject=message.get('Subject'),
        dateReceived=formatted_date
        ) 

        print(duplicate_email_check.exists())

        if duplicate_email_check.exists() is False:

            new_Email = Email(
                user = user,
                dateReceived = formatted_date,
                sender = from_sender,
                to = message.get('To'),
                subject = message.get('Subject'),
                message = message_text,
                read = False,
            )

            new_Email.save()
            print("E-Mail Saved")
        else:
            print("E-Mail already exists")

    imap.close()


# Already have emails then you create new client
@shared_task
def saving_client_emails(eml_value):
    print("\nAssigning Client to E-Mails:\n")

    emails_none = Email.objects.filter(clt=None)
    emails_filtered = emails_none.filter(sender=eml_value)
    print(f'\nE-Mails filtered to:\n {emails_filtered}')

    client = Client.objects.get(eml = eml_value)
    print(f'Clients found {client.name}')


    for email in emails_filtered:
        print('Assigning client: {client.name} to E-Mail ')
        email.clt = client
        email.save()



# First add client and when synching it will automatically add client name to email
