from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import AddStudentForm, AddStaffForm
from django.views.generic import View
from django.contrib.auth.models import User

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


def del_stu(request):
    if request.user.is_authenticated and request.user.is_staff:
            context={
                'objs':User.objects.filter(is_staff=False, is_superuser=False)
            }
            return render(request, 'console/jobs/delete_stu.html', context)

def del_stu_view(request, pk):
    if request.user.is_authenticated:
        if request.user.is_staff:
            obj = User.objects.filter(id=pk)
            obj.delete()
            return redirect('delete_stu')
        return redirect('dashboard')
   
def del_staff(request):
    if request.user.is_authenticated and request.user.is_staff:
            context={
                'objs':User.objects.filter(is_staff=True).exclude(username=request.user.username)
            }
            return render(request, 'console/jobs/delete_staff.html', context)

def del_staff_view(request, pk):
    if request.user.is_authenticated:
        if request.user.is_staff:
            obj = User.objects.filter(id=pk)
            obj.delete()
            return redirect('delete_staff')
        return redirect('dashboard')

def edit_user(request):
    if request.user.is_authenticated:
        if request.user.is_staff:
            return render(request, 'console/jobs/edit_user.html')