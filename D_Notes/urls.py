from django.contrib import admin
from django.urls import path
from . import views

app_name = 'notes'

urlpatterns = [
    path('add_note/', views.add_note, name="add_note"),
    path('read_note/', views.read_notes, name='read_note'),
    path('update_note/', views.update_note, name='update_note'),
    path('<int:note_id>', views.delete_note, name='delete_note'),

]
