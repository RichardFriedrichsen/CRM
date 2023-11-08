from django.forms import ModelForm
from .models import User


class add_config(ModelForm):
    class Meta:
        model = User
        fields = '__all__'
