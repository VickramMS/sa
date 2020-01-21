from django.urls import path
from console.views import grade

urlpatterns = [
    path('add/', grade.add, name='add_grade'),
    path('edit/', grade.elist, name='edit_grades'),
    path('edit/<pk>/', grade.edit, name='edit_grade_form'),
    path('delete/', grade.dlist, name='delete_grade'),
    path('delete/<pk>/', grade.delete, name='del_grade'),
]