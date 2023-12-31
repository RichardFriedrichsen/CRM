from django.forms import ModelForm
from .models import Note
from django import forms


class add_note_form(ModelForm):
    class Meta:
        model = Note
        fields = '__all__'
        exclude = ['createDate']
        widgets = {
            'deadline': forms.DateInput(attrs={'type': 'date'}),
        }
