from django.shortcuts import render, redirect, HttpResponseRedirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.http import HttpResponse
from django.views.generic import View
from django.utils import timezone 
from .models import Internal, Semester, SubjectAssign, SemAssign,Subject
from django.forms import modelformset_factory
from .forms import SubjectAssignForm, SemAssignForm

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

def assign_int(request):
    if request.user.is_staff:
        form=SubjectAssignForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('assign_int')
        return render(request, 'console/jobs/assign_int.html',{'form':form})
    else:
        return redirect('dashboard')

def assigned_class(request):
    if request.user.is_staff:  
        context={
            'classes': SubjectAssign.objects.filter(staff__username=request.user.username)
        }
        return render(request, 'console/academics/assigned_class.html', context)
    else:
        return redirect('internals')

def internals(request):
    if request.user.is_staff:  
        formset = modelformset_factory(Internal, fields=('student','marks1','marks2','marks3'), extra=0)
        search = request.GET.get('subject-query')
        if request.method == "POST":
            forms=formset(request.POST)
            if forms.is_valid():
                forms.save()
                return redirect('assigned_class')
        forms = formset(queryset=(Internal.objects.filter(subject__subcode=search)))
        return render(request, 'console/academics/internals.html',{'forms':forms})
    else:
        context={
            'internals1': Internal.objects.filter(student__username=request.user.username).filter(subject__sem=1),
            'internals2': Internal.objects.filter(student__username=request.user.username).filter(subject__sem=2),
            'internals3': Internal.objects.filter(student__username=request.user.username).filter(subject__sem=3),
            'internals4': Internal.objects.filter(student__username=request.user.username).filter(subject__sem=4),
            'internals5': Internal.objects.filter(student__username=request.user.username).filter(subject__sem=5),
            'internals6': Internal.objects.filter(student__username=request.user.username).filter(subject__sem=6),
            'internals7': Internal.objects.filter(student__username=request.user.username).filter(subject__sem=7),
            'internals8': Internal.objects.filter(student__username=request.user.username).filter(subject__sem=8),
        }
        return render(request, 'student/academics/internals.html',context)

def assign_sem(request):
    if request.user.is_staff:
        form=SemAssignForm(request.POST)
        if form.is_valid():
            SemAssign=form.save()
            return redirect('dashboard')
        return render(request, 'console/jobs/assign_sem.html',{'form':form})
    else:
        return redirect('dashboard')

def assigned_sem(request):
    if request.user.is_staff:  
        context={
            'classes': SemAssign.objects.filter(staff__username=request.user.username)
        }
        return render(request, 'console/academics/assigned_sem.html', context)
    else:
        return redirect('semesters')

def semesters(request):
    if request.user.is_staff: 
        formset = modelformset_factory(Semester, fields=('student','subject','grade','result'), extra=0)
        search = request.GET.get('subject-query')
        if request.method == "POST":
            forms=formset(request.POST)
            if forms.is_valid():
                forms.save()
                return redirect('assigned_sem')
        forms = formset(queryset=(Semester.objects.filter(subject__subcode=search))) 
        return render(request, 'console/academics/semesters.html', {'forms':forms})
    else:
        context={
            'semesters1': Semester.objects.filter(student__username=request.user.username).filter(subject__sem=1),
            'semesters2': Semester.objects.filter(student__username=request.user.username).filter(subject__sem=2),
            'semesters3': Semester.objects.filter(student__username=request.user.username).filter(subject__sem=3),
            'semesters4': Semester.objects.filter(student__username=request.user.username).filter(subject__sem=4),
            'semesters5': Semester.objects.filter(student__username=request.user.username).filter(subject__sem=5),
            'semesters6': Semester.objects.filter(student__username=request.user.username).filter(subject__sem=6),
            'semesters7': Semester.objects.filter(student__username=request.user.username).filter(subject__sem=7),
            'semesters8': Semester.objects.filter(student__username=request.user.username).filter(subject__sem=8),
        }
        return render(request, 'student/academics/semesters.html',context)


def profile(request):
    if request.user.is_staff:
        return render(request, 'console/profile.html',)
    else:
        return render(request, 'student/profile.html',)


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
