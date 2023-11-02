from django.shortcuts import render, redirect
from . configuration_from import add_config
# Create your views here.


def list_config(request):
    submitted = False

    if request.method == "POST":
        form = add_config(request.POST)
        if form.is_valid():
            form.save()
            return redirect('emails:list_emails')
    else:
        form = add_config()

    if 'submitted' in request.GET:
        submitted = True

    return render(request, "configuration.html", {"form": form, 'submitted': submitted})
