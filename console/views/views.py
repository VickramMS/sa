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

def assign_int(request):
    if request.user.is_staff:
        form=IntAssignForm(request.POST)
        if request.method == "GET":
            dept = request.GET.get('department')
            sem = request.GET.get('subject')
            form.fields['staff'].queryset = User.objects.filter(is_staff=True, profile__Department=dept)
            form.fields['subject'].queryset = Subject.objects.filter(sem=sem)
        if request.method == "POST":            
            if form.is_valid():
                form.save()
                return redirect('assign_int')
        return render(request, 'console/jobs/assign_int.html',{'form':form})
    else:
        return redirect('dashboard')

def assigned_int(request):
    if request.user.is_staff:  
        context={
            'classes': IntAssign.objects.filter(staff__username=request.user.username)
        }
        return render(request, 'console/academics/assigned_class.html', context)
    else:
        return redirect('internals')

def internals(request):
    if request.user.is_staff:  
        formset = modelformset_factory(Internal, fields=('student','marks1','marks2','marks3'), extra=0)
        if request.method == "GET":
            search = request.GET.get('subject-query')
            department = request.GET.get('department')
        if request.method == "POST":
            forms=formset(request.POST)
            if forms.is_valid():
                forms.save()
                return redirect('assigned_class')
        forms = formset(queryset=(Internal.objects.filter(subject__subcode=search, dept=department)))
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
        if request.method == "GET":
            dept = request.GET.get('department')
            sem = request.GET.get('subject')
            form.fields['staff'].queryset = User.objects.filter(is_staff=True, profile__Department=dept)
            form.fields['semester'].queryset = Subject.objects.filter(sem=sem)
        if request.method == "POST":            
            if form.is_valid():
                form.save()
                return redirect('assign_sem')
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
        if request.method == "GET":
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



def enroll_internal(request):
    if request.user.is_staff:
        form=InternalForm(request.POST)
        if request.method == "GET":
            dept = request.GET.get('department')
            sub = request.GET.get('semester')
            form.fields['student'].queryset = User.objects.filter(is_staff=False, is_superuser=False, profile__Department=dept)
            form.fields['subject'].queryset = Subject.objects.filter(sem=sub)
        if request.method == "POST":            
            if form.is_valid():
                form.save()
                messages.success(request, 'A new internal record has been updated!')
                return redirect('enroll_internal')
            else:
                print('form not valid')
        return render(request, 'console/academics/new_int.html',{'form':form})
    else:
        return redirect('dashboard')

def enroll_semester(request):
    if request.user.is_staff:
        form=SemesterForm(request.POST)
        if request.method == "GET":
            dept = request.GET.get('department')
            sub = request.GET.get('semester')
            form.fields['student'].queryset = User.objects.filter(is_staff=False, is_superuser=False, profile__Department=dept)
            form.fields['subject'].queryset = Subject.objects.filter(sem=sub)
        if request.method == "POST":            
            if form.is_valid():
                Semester=form.save()
                return redirect('enroll_semester')
            else:
                print('form not valid')
        return render(request, 'console/academics/new_sem.html',{'form':form})
    else:
        return redirect('dashboard')

def finish_int(request):
    if request.user.is_authenticated:
        if request.user.is_staff:
            context={
            'classes': IntAssign.objects.filter(staff__username=request.user.username)
            }
            return render(request, 'console/academics/finish_int.html', context)

def delete_int(request, id, id2):
    if request.user.is_authenticated:
        if request.user.is_staff:
            context={
            'objs': Internal.objects.filter(subject__subcode=id, dept=id2),
            'id':id,
            'id2':id2,
            }
            return render(request, 'console/academics/finish_int_del.html', context)

def delete_internal(request, id, id2):
    if request.user.is_authenticated:
        if request.user.is_staff:
            obj = IntAssign.objects.filter(subject__subcode=id, department=id2)
            obj.delete()
            return redirect('finish_int')
        else:
            return redirect('dashboard')

def finish_sem(request):
    if request.user.is_authenticated:
        if request.user.is_staff:
            context={
            'semesters': SemAssign.objects.filter(staff__username=request.user.username)
            }
            return render(request, 'console/academics/finish_sem.html', context)

def delete_sem(request, id, id2):
    if request.user.is_authenticated:
        if request.user.is_staff:
            context={
            'objs': Semester.objects.filter(subject__subcode=id, dept=id2),
            'id':id,
            'id2':id2,
            }
            return render(request, 'console/academics/finish_sem_del.html', context)

def delete_semester(request, id, id2):
    if request.user.is_authenticated:
        if request.user.is_staff:
            obj = SemAssign.objects.filter(semester__subcode=id, department=id2)
            obj.delete()
            return redirect('finish_sem')
        else:
            return redirect('dashboard')
