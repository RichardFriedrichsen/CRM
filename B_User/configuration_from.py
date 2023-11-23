from django import forms
from django.forms import ModelForm
from .models import User


class add_config(ModelForm):
    class Meta:
        model = User
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Enter your name','class': 'form-input-field'}),
            'surname': forms.TextInput(attrs={'placeholder': 'Enter your surname','class': 'form-input-field'}),
            'imap_server': forms.TextInput(attrs={'placeholder': 'IMAP Server','class': 'form-input-field'}),
            'imap_email': forms.EmailInput(attrs={'placeholder': 'IMAP Email','class': 'form-input-field'}),
            'imap_password': forms.PasswordInput(attrs={'placeholder': 'IMAP Password','class': 'form-input-field'}),
            'imap_port': forms.NumberInput(attrs={'placeholder': 'IMAP Port','class': 'form-input-field'}),
            'smtp_server': forms.TextInput(attrs={'placeholder': 'SMTP Server','class': 'form-input-field'}),
            'smtp_port': forms.NumberInput(attrs={'placeholder': 'SMTP Port','class': 'form-input-field'}),
        }