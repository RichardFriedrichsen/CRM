from django.shortcuts import render
from .tasks import mock_action

# Create your views here.


def list_emails(request):
    mock_action.delay()
    return render(request, "email.html")
