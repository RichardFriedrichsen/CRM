from django.db import models
# Create your models here.
from B_User.models import User


class Email(models.Model):
    _user = models.ForeignKey(User, on_delete=models.CASCADE)
    last_synched = models.DateField()
    _from = models.CharField(max_length=100)
    _to = models.CharField(max_length=100)
    _subject = models.CharField(max_length=100)
    message = models.TextField()
    read = models.BooleanField(default=False)

    def __str__(self):
        return f"{self._from} {self._subject}"
