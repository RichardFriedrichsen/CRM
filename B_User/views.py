from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from . configuration_from import add_config
from .models import User


def login_user(request):
    return render(request, 'authenticate/login.html')


def list_config(request):
    config = User.objects.first()
    print(config)
    submitted = False

    if request.method == "POST":
        form = add_config(request.POST, instance=config)
        if form.is_valid():
            form.save()
            return redirect('emails:list_emails')
    else:
        form = add_config(instance=config)

    if 'submitted' in request.GET:
        submitted = True

    return render(request, "configuration.html", {"form": form, 'submitted': submitted, 'config': config})
