from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from users import views as user_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    path('',views.home, name='home'),
    path('dashboard/', views.home, name='dashboard'),  
    path('academics/internals/', views.internals, name='internals'),
    path('academics/semesters/', views.semesters, name='semesters'),
    path('academics/assigned_class/', views.assigned_class, name='assigned_class'),
    path('academics/assigned_sem/', views.assigned_sem, name='assigned_sem'),
    path('resources/', views.resources, name='resources'), 
    path('profile/', views.profile, name='profile'),
    path('help/', views.help, name='help'), 
]