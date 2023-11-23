from django.shortcuts import render,redirect
from .models import Note
from .notes_form import add_note_form

# Create your views here.
def add_note(request):

    # if this is a POST request we need to process the form data
    if request.method == "POST":
        # create a form instance and populate it with data from the request:
        form = add_note_form(request.POST)
        # check whether it's valid:
        if form.is_valid():
            form.save()
            return redirect('notes:read_note')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = add_note_form()

    return render(request, "add_note.html", {"form": form})


def read_notes(request):
    todo_notes = Note.objects.filter(add_to_do = True)

    return render(request, "to_dos.html", {"todo_notes": todo_notes})

def update_note(request):
    pass

def delete_note(request):
    pass