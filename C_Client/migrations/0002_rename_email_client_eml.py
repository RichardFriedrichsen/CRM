# Generated by Django 4.2.7 on 2023-11-23 21:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('C_Client', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='client',
            old_name='email',
            new_name='eml',
        ),
    ]