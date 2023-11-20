from typing import Any
from django.db import models
from C_Client.models import Client 
# Create your models here.

class Note(models.Model):
    CREATE_CHOICES = [
        ('email', 'Email'),
        ('phone', 'Phone'),
        ('whatsapp', 'WhatsApp'),
    ]

    createDate = models.DateTimeField(auto_created=True)
    deadline = models.DateField()
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    contact_type = models.CharField(max_length=10, choices=CREATE_CHOICES)
    title = models.CharField(max_length=100)
    summary = models.TextField()
    add_to_do = models.BooleanField()

    def __str__(self) -> str:
        return f"{self.title} {self.createDate}"