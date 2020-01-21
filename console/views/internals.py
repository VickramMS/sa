from django.shortcuts import render, redirect
from console.models import Internal, IntAssign, Subject
from console.forms import InternalForm, IntAssignForm
from django.contrib.auth.models import User
from django.forms import modelformset_factory


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
        return render(request, 'console/internals/assign_int.html',{'form':form})
    else:
        return redirect('dashboard')

def assigned_int(request):
    if request.user.is_staff:  
        context={
            'classes': IntAssign.objects.filter(staff__username=request.user.username)
        }
        return render(request, 'console/internals/assigned_class.html', context)
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
        return render(request, 'console/internals/internals.html',{'forms':forms})
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
        return render(request, 'student/internals/internals.html',context)

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
                messages.success(request, 'A new internal record has been created!')
                return redirect('enroll_internal')
            else:
                print('form not valid')
        return render(request, 'console/internals/new_int.html',{'form':form})
    else:
        return redirect('dashboard')


def finish_int(request):
    if request.user.is_authenticated:
        if request.user.is_staff:
            context={
            'classes': IntAssign.objects.filter(staff__username=request.user.username)
            }
            return render(request, 'console/internals/finish_int.html', context)

def delete_int(request, id, id2):
    if request.user.is_authenticated:
        if request.user.is_staff:
            context={
            'objs': Internal.objects.filter(subject__subcode=id, dept=id2),
            'id':id,
            'id2':id2,
            }
            return render(request, 'console/internals/finish_int_del.html', context)

def delete_internal(request, id, id2):
    if request.user.is_authenticated:
        if request.user.is_staff:
            obj = IntAssign.objects.filter(subject__subcode=id, department=id2)
            obj.delete()
            return redirect('finish_int')
        else:
            return redirect('dashboard')
