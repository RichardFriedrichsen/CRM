from celery import shared_task
import time
from B_User.models import User

import imaplib
import email


def retrivingEmails():
    # Getting User Credentials
    server = User.objects.first().imap_server
    password = User.objects.first().imap_password
    email = User.objects.first().imap_email
    port = User.objects.first().imap_port

    # connection to the server
    imap = imaplib.IMAP4_SSL(server, port)
    imap.login(email, password)
    imap.select("Inbox")

    # Search Criteria
    _, msgnums = imap.search(None, "ALL")

    # Printing the number of E-Mails
    num_emails = len(msgnums[0].split())
    print(f"Number of emails in the inbox: {num_emails}")

    # for mgsnum in msgnums[0].split():
    #     _, data = imap.fetch(mgsnum, "(RFC822)")

    #     message = email.message_from_bytes(data[0][1])
    #     print(f"Message number: {mgsnum}")
    #     print(f"From: {message.get('From')}")
    #     print(f"To: {message.get('To')}")
    #     print(f"Date: {message.get('Date')}")
    #     print(f"Subject: {message.get('Subject')}")

    #     for part in message.walk():
    #         if part.get_content_type() == "text/plain":
    #             print(part.as_string())
    imap.close()


@shared_task
def mock_action():
    print("Testing task")
    time.sleep(15)
    print("Testing task")
