from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from .models import Client
from .forms import add_client_form
# Create your views here.


def add_client(request):

    # if this is a POST request we need to process the form data
    if request.method == "POST":
        # create a form instance and populate it with data from the request:
        form = add_client_form(request.POST)
        # check whether it's valid:
        if form.is_valid():
            form.save()
            return redirect('emails:list_emails')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = add_client_form()

    return render(request, "add_client.html", {"form": form})


def read_clients(request):
    all_clients = Client.objects.all()

    return render(request, "read_clients.html", {"all_clients": all_clients})
