from django.shortcuts import render, redirect, get_object_or_404
from console.models import Subject
from django.contrib import messages

def add(request):
    if request.user.is_staff:
        if request.method == "POST":
            subject = Subject()
            subject.subname = request.POST.get("subname")
            subject.subcode = request.POST.get("subcode")
            subject.subcred = request.POST.get("subcred")
            subject.sem = request.POST.get("sem")
            subject.save()
            messages.success(request, 'New Subject has been added!')
            return redirect('add_subject')
        return render(request, 'console/subjects/add.html')
    else:
        return redirect('dashboard')

def elist(request):
    if request.user.is_authenticated:
        if request.user.is_staff:
            context={
                'subjects': Subject.objects.all()
            }
            return render(request, 'console/subjects/list.html', context)
        else:
            return redirect('dashboard')

def edit(request, pk):
    if request.user.is_staff:
        obj = Subject.objects.get(id=pk)
        context = {
            "obj": obj
        }
        if request.method == "POST":
            obj.subname = request.POST.get("subname")
            obj.subcode = request.POST.get("subcode")
            obj.subcred = request.POST.get("subcred")
            obj.sem = request.POST.get("sem")
            obj.save()
            messages.warning(request, 'Subject records has been updated!')
            return redirect('edit_sub')
        return render(request, 'console/subjects/edit.html', context)
    else:
        return redirect('edit_sub')

def dlist(request):
    if request.user.is_authenticated:
        if request.user.is_staff:
            context={
                'subjects': Subject.objects.all()
            }
            return render(request, 'console/subjects/delete.html', context)
        else:
            return redirect('dashboard')

def delete(request, pk):
    if request.user.is_authenticated:
        if request.user.is_staff:
            obj = Subject.objects.get(id=pk)
            obj.delete()
            messages.error(request, 'Subject record has been deleted!')
            return redirect('delete_sub')
        return redirect('dashboard')
   