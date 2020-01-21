from django.shortcuts import render, redirect, HttpResponseRedirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.http import HttpResponse
from django.views.generic import View
from django.utils import timezone 
from console.models import Internal, Semester, IntAssign, SemAssign, Grade
from django.forms import modelformset_factory
from console.forms import IntAssignForm, SemAssignForm, InternalForm, SemesterForm
from django.contrib import messages

def home(request):
    if request.user.is_authenticated:
        if request.user.is_superuser:
            return render(request, 'console/su-dashboard.html')
        elif request.user.is_staff:
            return render(request, 'console/dashboard.html')
        else:
            return render(request, 'student/dashboard.html')
    else:
        return render(request, 'console/home.html')