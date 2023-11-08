from celery import shared_task
import time


def retrivingEmails():
    pass


@shared_task
def mock_action():
    print("Testing task")
    time.sleep(15)
    print("Testing task")
