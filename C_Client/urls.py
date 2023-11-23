from django.contrib import admin
from django.urls import path
from . import views

app_name = 'client'

urlpatterns = [
    path('add_client/', views.add_client, name="add_client"),
    path('read_clients/', views.read_clients, name="read_clients"),
    path('<int:client_id>/', views.delete_client, name="delete_client"),
]
