from django.shortcuts import render
from .tasks import retrivingEmails
from .models import Email

# Create your views here.


def list_emails(request):
    retrivingEmails()
    read_emails = Email.objects.all()

    return render(request, "email.html", {"read_emails": read_emails})
