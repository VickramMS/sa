"""student_analytica URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from users import views as user_views
from console.views import views as console_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', console_views.home, name='home'),
    path('dashboard/', console_views.home, name='dashboard'),  
    path('subject/', include('console.urls.subject')),
    path('grade/', include('console.urls.grade')),
    path('internal/', include('console.urls.internals')),
    path('semester/', include('console.urls.semesters')),
    path('user/', include('users.urls')),
    path('login/', user_views.Login.as_view(),name='login'),
    path('logout/', user_views.LogoutView.as_view(), name='logout'),
    path('error404/', console_views.page404, name="page404")
]
