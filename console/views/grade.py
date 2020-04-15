from django.shortcuts import render, redirect, get_object_or_404
from console.models import Grade
from django.contrib import messages


def add(request):
    if request.user.is_staff:
        if request.method == "POST":
            grade = Grade()
            grade.points = request.POST.get("points")
            grade.letter = request.POST.get("letter")
            grade.save()
            messages.success(request, 'New Grade has been added!')
            return redirect('add_grade')
        return render(request, 'console/grades/add.html')
    else:
        return redirect('dashboard')

def elist(request):
    if request.user.is_authenticated:
        if request.user.is_staff:
            context={
                'grades': Grade.objects.all()
            }
            return render(request, 'console/grades/list.html', context)
        else:
            return redirect('dashboard')

    
def edit(request, pk):
    if request.user.is_staff:
        obj = Grade.objects.get(id=pk)
        if request.method == "GET":
            context = {
                "obj": obj
            }
        if request.method == "POST":
            obj.points = request.POST.get("points")
            obj.letter = request.POST.get("letter")
            obj.save()
            messages.warning(request, 'Grade records has been updated!')
            return redirect('edit_grades')
        return render(request, 'console/grades/edit.html', context)
    else:
        return redirect('edit_grades')

def dlist(request):
    if request.user.is_authenticated:
        if request.user.is_staff:
            context={
                'grades': Grade.objects.all()
            }
            return render(request, 'console/grades/delete.html', context)
        else:
            return redirect('dashboard')

def delete(request, pk):
    if request.user.is_authenticated:
        if request.user.is_staff:
            obj = Grade.objects.get(id=pk)
            obj.delete()
            messages.error(request, 'Grade record has been deleted!')
            return redirect('delete_grade')
        return redirect('dashboard')
