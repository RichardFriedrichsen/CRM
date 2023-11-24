from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect
from .models import Client
from .forms import add_client_form

from A_Email.tasks import saving_client_emails
# Create your views here.


################## Adding Client #########################
def add_client(request):

    # if this is a POST request we need to process the form data
    if request.method == "POST":
        # create a form instance and populate it with data from the request:
        form = add_client_form(request.POST)
        # check whether it's valid:
        if form.is_valid():
            eml_value = form.cleaned_data['eml']
            form.save()
            saving_client_emails(eml_value)
            return redirect('client:read_clients')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = add_client_form()

    return render(request, "add_client.html", {"form": form})

################## Reading Clients #########################
def read_clients(request):
    all_clients = Client.objects.all()

    return render(request, "read_clients.html", {"all_clients": all_clients})

################## Updating Client #########################
def update_client(request, client_id):
    client = get_object_or_404(Client, pk = client_id)
    
    submitted = False

    if request.method == "POST":
        form = add_client_form(request.POST, instance=client)
        if form.is_valid():
            form.save()
            return redirect('client:read_clients')
    else:
        form = add_client_form(instance=client)

    if 'submitted' in request.GET:
        submitted = True

    return render(request, "add_client.html", {"form": form, 'submitted': submitted, 'client': client}) 


################## Deleting Client #########################

def delete_client(request, client_id):
    client = get_object_or_404(Client, pk = client_id)
    client.delete()

    return redirect('client:read_clients')
    
