from django.contrib import admin
from django.urls import path
from . import views

app_name = 'notes'

urlpatterns = [
    path('add_note/', views.add_note, name="add_note"),
]
