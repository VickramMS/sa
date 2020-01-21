from django.urls import path
from console.views import subject

urlpatterns = [
    path('jobs/add_subject/', subject.add_subject, name='add_subject'),
    path('jobs/edit_sub/', subject.edit_sub, name='edit_sub'),
    path('jobs/edit_sub/<pk>/', subject.edit_sub_view, name='edit_sub_form'),
    path('jobs/delete_sub/', subject.delete_sub, name='delete_sub'),
    path('jobs/delete_sub/<pk>/', subject.delete_sub_view, name='delete_sub_form'),
]