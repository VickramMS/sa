from django.shortcuts import render, redirect
from console.models import Semester, SemAssign, Subject
from console.forms import SemesterForm, SemAssignForm
from users.models import User
from django.forms import modelformset_factory
from django.contrib import messages

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
        return render(request, 'console/semesters/assign_sem.html',{'form':form})
    else:
        return redirect('dashboard')

def assigned_sem(request):
    if request.user.is_staff:  
        context={
            'classes': SemAssign.objects.filter(staff__username=request.user.username)
        }
        return render(request, 'console/semesters/assigned_sem.html', context)
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
        return render(request, 'console/semesters/semesters.html', {'forms':forms})
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
        return render(request, 'student/semesters/semesters.html',context)

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
        return render(request, 'console/semesters/new_sem.html',{'form':form})
    else:
        return redirect('dashboard')


def finish_sem(request):
    if request.user.is_authenticated:
        if request.user.is_staff:
            context={
            'semesters': SemAssign.objects.filter(staff__username=request.user.username)
            }
            return render(request, 'console/semesters/finish_sem.html', context)

def delete_sem(request, id, id2):
    if request.user.is_authenticated:
        if request.user.is_staff:
            context={
            'objs': Semester.objects.filter(subject__subcode=id, dept=id2),
            'id':id,
            'id2':id2,
            }
            return render(request, 'console/semesters/finish_sem_del.html', context)

def delete_semester(request, id, id2):
    if request.user.is_authenticated:
        if request.user.is_staff:
            obj = SemAssign.objects.filter(semester__subcode=id, department=id2)
            obj.delete()
            return redirect('finish_sem')
        else:
            return redirect('dashboard')