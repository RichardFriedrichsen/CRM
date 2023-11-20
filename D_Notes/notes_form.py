from django.forms import ModelForm
from .models import Note


class add_note_form(ModelForm):
    class Meta:
        model = Note
        fields = '__all__'
        exclude = ['createDate']
