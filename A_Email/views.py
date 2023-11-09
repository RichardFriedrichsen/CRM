from django.shortcuts import render
from .tasks import mock_action, retrivingEmails

# Create your views here.


def list_emails(request):
    retrivingEmails()
    mock_action.delay()
    return render(request, "email.html")
