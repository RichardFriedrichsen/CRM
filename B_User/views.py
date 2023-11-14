from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.contrib import messages
from . configuration_from import add_config
from .models import User


def login_user(request):

    # If the method is post, otherwise it would be get
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        # If authenticate works then we have a User and it's not none
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse('emails:list_emails'))

        # If the login fails
        else:

            return HttpResponseRedirect(reverse('user:login_user'))

    # If we have a GET request
    else:
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
