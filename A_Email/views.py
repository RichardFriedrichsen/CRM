from django.shortcuts import render

# Create your views here.


def list_emails(request):
    return render(request, "email.html")
