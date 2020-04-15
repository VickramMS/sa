from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import AddStudentForm, AddStaffForm
from django.views.generic import View
from users.models import User
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import authenticate, login, logout

class Login(View):
    template_name="console/home.html"
    def get(self,request):
        return render(request,self.template_name)
    def post(self,request):
        try:
            user =User.objects.get(email=request.POST.get('email'))            
        except:
            return render(request, self.template_name,{'error':True})   
        else:
            user = authenticate(request,username=user.username,password=request.POST.get('password'))
            if user is None:
                return render(request,self.template_name,{'error':True})
            login(request,user)
            response= redirect('dashboard')
            response.set_cookie('role','user')
            return response
        return render(request,self.template_name)


class LogoutView(View,LoginRequiredMixin):
    def get(self,request):  
        logout(request)
        response=redirect('home')
        response.delete_cookie('role')
        return response


def add_student(request):
    if request.method == 'POST':
        user = User()
        user.username = request.POST.get('username')
        user.email = request.POST.get('email')
        user.user_type = request.POST.get('user-type')
        user.department = request.POST.get('department')
        user.date_of_birth = request.POST.get('date-of-birth')
        dob = user.date_of_birth
        year = str(dob)[0:4]
        month = str(dob)[5:7]
        date = str(dob)[8:10]
        user.set_password(str(date+'-'+month+'-'+year))
        user.save()
        messages.success(request, 'A new student has been created!')
        return redirect('add_student')
    return render(request, 'console/users/add_student.html')

def add_staff(request):
    if request.method == 'POST':
        user = User()
        user.username = request.POST.get('username')
        user.email = request.POST.get('email')
        user.user_type = request.POST.get('user-type')
        user.department = request.POST.get('department')
        user.password = request.POST.get('password')
        user.set_password(str(user.password))
        user.save()
        messages.success(request, 'A new staff has been created!')
        return redirect('add_staff')
    return render(request, 'console/users/add_staff.html')


def del_stu(request):
    if request.user.is_authenticated and request.user.is_staff:
            context={
                'objs':User.objects.filter(is_staff=False, is_superuser=False)
            }
            return render(request, 'console/users/delete_stu.html', context)

def del_stu_view(request, pk):
    if request.user.is_authenticated:
        if request.user.is_staff:
            obj = User.objects.filter(id=pk)
            obj.delete()
            messages.error(request, 'Student record has been added!')
            return redirect('delete_stu')
        return redirect('dashboard')
   
def del_staff(request):
    if request.user.is_authenticated and request.user.is_staff:
            context={
                'objs':User.objects.filter(is_staff=True).exclude(username=request.user.username)
            }
            return render(request, 'console/users/delete_staff.html', context)

def del_staff_view(request, pk):
    if request.user.is_authenticated:
        if request.user.is_staff:
            obj = User.objects.filter(id=pk)
            obj.delete()
            messages.error(request, 'Staff record has been added!')
            return redirect('delete_staff')
        return redirect('dashboard')
