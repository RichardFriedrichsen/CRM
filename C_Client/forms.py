from django.forms import ModelForm
from .models import Client


class add_client_form(ModelForm):
    class Meta:
        model = Client
        fields = '__all__'
