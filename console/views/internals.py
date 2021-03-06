from django.shortcuts import render, redirect
from console.models import Internal, IntAssign, Subject
from users.models import User
from django.forms import modelformset_factory
from django.contrib import messages


def assign_internals(request):
    if request.user.user_type == "ADMIN" or request.user.user_type == "":
        if request.method == "GET":
            dept = request.GET.get('department')
            sem = request.GET.get('semesters')
            context = {
            "userobjs" : User.objects.filter(user_type="STAFF" or "HOD", department=dept),
            "subjectobjs" : Subject.objects.filter(sem=sem)
            }
        if request.method == "POST":
            assign = IntAssign()
            assign.staff = User.objects.get(id=request.POST.get("staff"))
            assign.subject = Subject.objects.get(id=request.POST.get("subject"))
            assign.department = request.POST.get("department")
            assign.save()
            messages.success(request, 'Internal job has been assigned!')
            return redirect('assign_internals')
        return render(request, 'console/internals/assign_internal.html',context)
    else:
        return redirect('dashboard')

def assigned_internals(request):
    if request.user.user_type == "ADMIN" or request.user.user_type == "" or request.user.user_type == "STAFF" or request.user.user_type == "HOD":
        context={
            'classes': IntAssign.objects.filter(staff__username=request.user.username)
        } 
        return render(request, 'console/internals/assigned_internal.html', context)
    elif request.user.user_type == "STUDENT" or request.user.user_type == "REPRESENTATIVE":
        return redirect('internals')

def internals(request):
    if  request.user.user_type == "ADMIN" or request.user.user_type == "" or request.user.user_type == "STAFF" or request.user.user_type == "HOD":
        formset = modelformset_factory(Internal, fields=('student','marks1','marks2','marks3'), extra=0)
        search = request.GET.get('subject-query')
        department = request.GET.get('department')
        if request.method == "POST":
            forms=formset(request.POST)
            if forms.is_valid():
                forms.save()
                return redirect('assigned_class')
        forms = formset(queryset=(Internal.objects.filter(subject__subcode=search, dept=department)))
        return render(request, 'console/internals/internals.html',{'forms':forms})
    elif request.user.user_type == "STUDENT" or request.user.user_type == "REPRESENTATIVE":
        print("rtue") 
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

def enroll_internal(request):
    if request.user.user_type == "STAFF" or request.user.user_type == "HOD" or request.user.user_type == "ADMIN" or request.user.user_type == "":
        if request.method == "GET":
            dept = request.GET.get('department')
            sub = request.GET.get('semester')
            context = {
            "studentobjs" : User.objects.filter(user_type="STUDENT" or "REPRESENTATIVE", department=dept),
            "subjectobjs": Subject.objects.filter(sem=sub)
            }
        if request.method == "POST":
            internals = Internal()
            internals.student = User.objects.get(id=request.POST.get("student"))
            internals.subject = Subject.objects.get(id=request.POST.get("subject"))
            internals.save()
            messages.success(request, 'A new internal record has been created!')
            return redirect('enroll_internal')
        return render(request, 'console/internals/enroll_internal.html', context)
    elif request.user.user_type == "STUDENT" or request.user.user_type == "REPRESENTATIVE":
        return redirect('dashboard')
    else:
        return redirect("page404")


def finish_internals(request):
    if request.user.is_authenticated:
        if request.user.user_type == "STAFF" or request.user.user_type == "HOD" or request.user.user_type == "ADMIN" or request.user.user_type == "":
            context={
            'classes': IntAssign.objects.filter(staff__username=request.user.username)
            }
            return render(request, 'console/internals/finish_int.html', context)

def delete_internal(request, id, id2):
    if request.user.is_authenticated:
        if request.user.user_type == "STAFF" or request.user.user_type == "HOD" or request.user.user_type == "ADMIN" or request.user.user_type == "":
            context={
            'objs': Internal.objects.filter(subject__subcode=id, dept=id2),
            'id':id,
            'id2':id2,
            }
            return render(request, 'console/internals/finish_int_del.html', context)

def delete_internals(request, id, id2):
    if request.user.is_authenticated:
        if request.user.user_type == "STAFF" or request.user.user_type == "HOD" or request.user.user_type == "ADMIN" or request.user.user_type == "":
            obj = IntAssign.objects.filter(subject__subcode=id, department=id2)
            obj.delete()
            return redirect('finish_int')
        else:
            return redirect('dashboard')
