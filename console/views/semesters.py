from django.shortcuts import render, redirect
from console.models import Semester, SemAssign, Subject
from console.forms import SemesterForm
from users.models import User
from django.forms import modelformset_factory
from django.contrib import messages

def assign_semesters(request):
    if request.user.user_type == "ADMIN" or request.user.user_type == "":
        if request.method == "GET":
            dept = request.GET.get('department')
            sem = request.GET.get('semester')
            context = {
            "userobjs": User.objects.filter(user_type="STAFF" or "HOD", department=dept),
            "subjectobjs": Subject.objects.filter(sem=sem)
            }
        if request.method == "POST":
            assign = SemAssign()
            assign.staff = User.objects.get(id=request.POST.get("staff"))
            assign.semester = Subject.objects.get(id=request.POST.get("semester"))
            assign.department = request.POST.get("department")
            assign.save()
            messages.success(request, 'Semester job has been assigned!')
            return redirect('assign_semesters')
        return render(request, 'console/semesters/assign_semester.html', context)
    else:
        return redirect('dashboard')

def assigned_semesters(request):
    if request.user.user_type == "ADMIN" or request.user.user_type == "" or request.user.user_type == "STAFF" or request.user.user_type == "HOD":  
        context={
            'classes': SemAssign.objects.filter(staff__username=request.user.username)
        }
        return render(request, 'console/semesters/assigned_semester.html', context)
    elif request.user.user_type == "STUDENT" or request.user.user_type == "REPRESENTATIVE":
        return redirect('semesters')

def semesters(request):
    if  request.user.user_type == "ADMIN" or request.user.user_type == "" or request.user.user_type == "STAFF" or request.user.user_type == "HOD": 
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
    elif request.user.user_type == "STUDENT" or request.user.user_type == "REPRESENTATIVE":
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

def enroll_semester(request):
    if request.user.user_type == "STAFF" or request.user.user_type == "HOD" or request.user.user_type == "ADMIN" or request.user.user_type == "":
        form=SemesterForm(request.POST)
        if request.method == "GET":
            dept = request.GET.get('department')
            sub = request.GET.get('semester')
            context = {
            "userobjs" : User.objects.filter(user_type="STUDENT" or "REPRESENTATIVE", department=dept),
            "subjectobjs": Subject.objects.filter(sem=sub)
            }
        if request.method == "POST":
            semester = Semester()
            semester.student = User.objects.get(id=request.POST.get("student"))
            semester.subject = Subject.objects.get(id=request.POST.get("subject"))
            semester.save()            
            messages.success(request, 'A new semester record has been created!')
            return redirect('enroll_semester')
        return render(request, 'console/semesters/enroll_semester.html', context)
    elif request.user.user_type == "STUDENT" or request.user.user_type == "REPRESENTATIVE":
        return redirect('dashboard')
    else:
        return redirect("page404")


def finish_semesters(request):
    if request.user.is_authenticated:
        if request.user.user_type == "STAFF" or request.user.user_type == "HOD" or request.user.user_type == "ADMIN" or request.user.user_type == "":
            context={
            'semesters': SemAssign.objects.filter(staff__username=request.user.username)
            }
            return render(request, 'console/semesters/finish_sem.html', context)

def delete_semester(request, id, id2):
    if request.user.is_authenticated:
        if request.user.user_type == "STAFF" or request.user.user_type == "HOD" or request.user.user_type == "ADMIN" or request.user.user_type == "":
            context={
            'objs': Semester.objects.filter(subject__subcode=id, dept=id2),
            'id':id,
            'id2':id2,
            }
            return render(request, 'console/semesters/finish_sem_del.html', context)

def delete_semesters(request, id, id2):
    if request.user.is_authenticated:
        if request.user.user_type == "STAFF" or request.user.user_type == "HOD" or request.user.user_type == "ADMIN" or request.user.user_type == "":
            obj = SemAssign.objects.filter(semester__subcode=id, department=id2)
            obj.delete()
            return redirect('finish_sem')
        else:
            return redirect('dashboard')