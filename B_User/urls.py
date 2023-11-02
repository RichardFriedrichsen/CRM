from django.contrib import admin
from django.urls import path
from . import views

app_name = 'user'

urlpatterns = [
    path('configuration/', views.list_config, name="list_config"),
]
