from django.db import models

# Create your models here.


class Client(models.Model):
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    eml = models.EmailField()
    phone = models.CharField(max_length=50)
    

    def __str__(self):
        return f"{self.name} {self.surname}"

