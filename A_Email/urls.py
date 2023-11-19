from django.contrib import admin
from django.urls import path
from . import views

app_name = 'emails'

urlpatterns = [
    path('', views.list_emails, name="list_emails"),
    path('<int:email_id>/', views.read_mail, name="read_mail"),
]
