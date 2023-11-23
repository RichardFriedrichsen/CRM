from django.forms import ModelForm
from .models import Client
from django import forms

class add_client_form(ModelForm):
    class Meta:
        model = Client
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Enter the name','class': 'form-input-field'}),
            'surname': forms.TextInput(attrs={'placeholder': 'Enter the surname','class': 'form-input-field'}),
            'eml': forms.TextInput(attrs={'placeholder': 'Enter the E-mail','class': 'form-input-field'}),
            'phone': forms.TextInput(attrs={'placeholder': 'Enter the phone','class': 'form-input-field'}),

    }