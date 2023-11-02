from django.db import models

# Create your models here.


class User(models.Model):
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    imap_server = models.CharField(max_length=50)
    imap_email = models.EmailField()
    imap_password = models.CharField(max_length=50)
