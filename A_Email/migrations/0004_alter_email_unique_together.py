# Generated by Django 4.2.7 on 2023-11-18 16:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('A_Email', '0003_rename_last_synched_email_datereceived'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='email',
            unique_together={('sender', 'subject', 'dateReceived')},
        ),
    ]
