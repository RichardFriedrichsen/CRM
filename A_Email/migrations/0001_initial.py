# Generated by Django 4.1.7 on 2023-10-30 11:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('B_User', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Email',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_synched', models.DateField()),
                ('_from', models.CharField(max_length=100)),
                ('_to', models.CharField(max_length=100)),
                ('_subject', models.CharField(max_length=100)),
                ('message', models.TextField()),
                ('read', models.BooleanField(default=False)),
                ('_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='B_User.user')),
            ],
        ),
    ]
