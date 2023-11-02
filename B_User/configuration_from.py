from django.forms import ModelForm
from .models import User


class add_config(ModelForm):
    class Meta:
        model = User
        fields = ('imap_server', 'imap_email', 'imap_password')
