from django.urls import path
from console.views import views, subject
from django.contrib.auth import views as auth_views
from users import views as user_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    path('',views.home, name='home'),
    path('dashboard/', views.home, name='dashboard'),  
    path('academics/internals/', views.internals, name='internals'),
    path('academics/finish_int/', views.finish_int, name='finish_int'),
    path('academics/finish_int/<id>/<id2>/', views.delete_int, name='delete_int'),
    path('academics/finish_int/<id>/<id2>/delete/', views.delete_internal, name='delete_internal'),

    path('academics/semesters/', views.semesters, name='semesters'),
    path('academics/finish_sem/', views.finish_sem, name='finish_sem'),
    path('academics/finish_sem/<id>/<id2>/', views.delete_sem, name='delete_sem'),
    path('academics/finish_sem/<id>/<id2>/delete/', views.delete_semester, name='delete_semester'),

    path('academics/assigned_class/', views.assigned_int, name='assigned_class'),
    path('academics/assigned_sem/', views.assigned_sem, name='assigned_sem'),
    
    path('jobs/assign_int/', views.assign_int, name='assign_int'),
    path('jobs/assign_sem/', views.assign_sem, name='assign_sem'),

    path('jobs/delete_user/', views.delete_user, name='delete_user'),
    path('jobs/enroll_internal/', views.enroll_internal, name='enroll_internal'),
    path('jobs/enroll_semester/', views.enroll_semester, name='enroll_semester'),
    path('profile/', views.profile, name='profile'),
]