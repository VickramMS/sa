from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from users import views as user_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    path('',views.home, name='home'),
    path('dashboard/', views.home, name='dashboard'),  
    path('academics/', views.academics, name='academics'), 
    path('academics/internals/', views.internals, name='internals'),
    path('academics/semesters/', views.semesters, name='semesters'),
    path('resources/', views.resources, name='resources'), 
    path('profile/', views.profile, name='profile'),
    path('help/', views.help, name='help'), 
]