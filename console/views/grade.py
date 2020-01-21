from django.shortcuts import render, redirect, get_object_or_404
from console.models import Grade
from console.forms import GradeForm
from django.contrib import messages


def add(request):
    if request.user.is_staff:
        form=GradeForm(request.POST)
        if form.is_valid():
            Grade=form.save()
            messages.success(request, 'New Grade has been added!')
            return redirect('add_grade')
        return render(request, 'console/grades/add.html',{'form':form})
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
        obj = get_object_or_404(Grade, id=pk)
        form = GradeForm(request.POST or None, instance=obj)
        context = {'form':form}
        if form.is_valid():
            obj = form.save(commit=False)
            obj.save()
            context = {'form':form}
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
            obj = Grade.objects.filter(id=pk)
            obj.delete()
            messages.error(request, 'Grade record has been deleted!')
            return redirect('delete_grade')
        return redirect('dashboard')
