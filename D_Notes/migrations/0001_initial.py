# Generated by Django 4.2.7 on 2023-11-20 16:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('C_Client', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Note',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('createDate', models.DateTimeField(auto_created=True)),
                ('deadline', models.DateField()),
                ('contact_type', models.CharField(choices=[('email', 'Email'), ('phone', 'Phone'), ('whatsapp', 'WhatsApp')], max_length=10)),
                ('title', models.CharField(max_length=100)),
                ('summary', models.TextField()),
                ('add_to_do', models.BooleanField()),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='C_Client.client')),
            ],
        ),
    ]