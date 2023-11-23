from django.db import models
# Create your models here.
from B_User.models import User as Usr
from C_Client.models import Client as clt


class Email(models.Model):
    user = models.ForeignKey(Usr, on_delete=models.CASCADE)
    clt = models.ForeignKey(clt, on_delete=models.CASCADE, null=True)
    dateReceived = models.DateTimeField()
    sender = models.CharField(max_length=100)
    to = models.CharField(max_length=100)
    subject = models.CharField(max_length=100)
    message = models.TextField()
    todo = models.BooleanField(default=False)
    read = models.BooleanField(default=False)

    class Meta:
        unique_together = ('sender', 'subject', 'dateReceived')

    def __str__(self):
        return f"{self.sender} {self.subject}"
