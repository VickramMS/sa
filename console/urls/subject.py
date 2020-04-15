from django.urls import path
from console.views import subject

urlpatterns = [
    path('add/', subject.add, name='add_subject'),
    path('edit/', subject.elist, name='edit_sub'),
    path('edit/<pk>/', subject.edit, name='edit_sub_form'),
    path('delete/', subject.dlist, name='delete_sub'),
    path('delete/<pk>/', subject.delete, name='delete_subject'),
]