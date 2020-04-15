from django.shortcuts import render
from users.models import User

def home(request):
    if request.user.is_authenticated:
        if request.user.user_type == "" or request.user.user_type == "ADMIN":
            return render(request, 'console/su-dashboard.html')
        elif request.user.user_type == "HOD" or request.user.user_type == "STAFF":
            return render(request, 'console/dashboard.html')
        elif request.user.user_type == "STUDENT" or request.user.user_type == "REPRESENTATIVE":
            return render(request, 'console/temp.html')
        else:
            return render(request, '404.html')
    else:
        return render(request, 'console/home.html')

def page404(request):
    return render(request, "404.html")