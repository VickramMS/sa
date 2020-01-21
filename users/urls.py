from django.urls import path, include
from . import views

urlpatterns = [
    path('add_student/', views.add_student, name='add_student'),
    path('add_staff/', views.add_staff, name='add_staff'),
    path('delete_stu/', views.del_stu, name='delete_stu'),
    path('delete_stu/<pk>/', views.del_stu_view, name='delete_stu_form'),
    path('delete_staff/', views.del_staff, name='delete_staff'),
    path('delete_staff/<pk>/', views.del_staff_view, name='delete_staff_form'),
]