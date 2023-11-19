from django.shortcuts import render, get_object_or_404
from .tasks import retrivingEmails
from .models import Email

# Create your views here.


def list_emails(request):
    retrivingEmails()
    read_emails = Email.objects.all()

    return render(request, "email.html", {"read_emails": read_emails})

def read_mail(request, email_id):
    email = Email.objects.get(pk=email_id)

    print(email.subject)
    return render(request, "email_detail.html", {'email': email})
