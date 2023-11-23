from django.shortcuts import render,redirect, get_object_or_404
from .models import Note
from .notes_form import add_note_form

############# Adding Notes ##########################
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

############# Reading Notes ##########################

def read_notes(request):
    todo_notes = Note.objects.filter(add_to_do = True)

    return render(request, "to_dos.html", {"todo_notes": todo_notes})

############# Updating Note ##########################

def update_note(request, note_id):
    note = get_object_or_404(Note, pk = note_id)
    
    submitted = False

    if request.method == "POST":
        form = add_note_form(request.POST, instance=note)
        if form.is_valid():
            form.save()
            return redirect('notes:read_note')
    else:
        form = add_note_form(instance=note)

    if 'submitted' in request.GET:
        submitted = True

    return render(request, "add_note.html", {"form": form, 'submitted': submitted, 'note': note}) 

############# Deleting Note ##########################

def delete_note(request, note_id):
    note = get_object_or_404(Note, pk = note_id)
    note.delete()
    
    return redirect('notes:read_note') 