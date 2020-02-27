from django.shortcuts import render
from users.models import User

def home(request):
    if request.user.is_authenticated:
        if request.user.user_type == "":
            return render(request, 'console/su-dashboard.html')
        if request.user.user_type == "ADMIN":
            return render(request, 'console/su-dashboard.html')
        elif request.user.user_type == "HOD":
            return render(request, 'console/dashboard.html')
        elif request.user.user_type == "STAFF":
            return render(request, 'console/dashboard.html')
        else:
            return render(request, 'console/temp.html')
    else:
        return render(request, 'console/home.html')