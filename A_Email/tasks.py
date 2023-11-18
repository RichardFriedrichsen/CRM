from celery import shared_task
import time
from datetime import date

from B_User.models import User
from C_Client.models import Client
from .models import Email

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

        message = email_parser.message_from_bytes(data[0][1])
        message_text = ""

        for part in message.walk():
            if part.get_content_type() == "text/plain":
                message_text += part.as_string()

        # Creating a new instance of an E-Mail
        new_Email = Email(
            user=user,
            last_synched=date.today(),
            sender=message.get('From'),
            to=message.get('To'),
            subject=message.get('Subject'),
            message=message_text,
            read=False,
        )

        new_Email.save()
        print("E-Mail Saved")

        print(f"Date: {message.get('Date')}")

    imap.close()
