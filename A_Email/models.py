from django.db import models
# Create your models here.
from B_User.models import User as Usr


class Email(models.Model):
    user = models.ForeignKey(Usr, on_delete=models.CASCADE)
    dateReceived = models.DateTimeField()
    sender = models.CharField(max_length=100)
    to = models.CharField(max_length=100)
    subject = models.CharField(max_length=100)
    message = models.TextField()
    read = models.BooleanField(default=False)

    class Meta:
        unique_together = ('sender', 'subject', 'dateReceived')

    def __str__(self):
        return f"{self.sender} {self.subject}"
