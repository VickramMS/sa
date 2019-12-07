from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import AddStudentForm, AddStaffForm
from django.views.generic import View

def add_student(request):
    if request.method == 'POST':
        form = AddStudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('add_student')
    else:
        form = AddStudentForm()
    return render(request, 'console/jobs/add_student.html', {'form': form})

def add_staff(request):
    if request.method == 'POST':
        form = AddStaffForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('add_staff')
    else:
        form = AddStaffForm()
    return render(request, 'console/jobs/add_staff.html', {'form': form})

