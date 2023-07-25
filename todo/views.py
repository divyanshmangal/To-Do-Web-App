from django.shortcuts import render,redirect
from .models import Task
from django.http import Http404
from django.shortcuts import get_object_or_404
# Create your views here.
def add_task(request):
    tasks=request.POST['task']
    Task.objects.create(task=tasks)
    return redirect('home')
def complete_task(request,pk):
    tasks=get_object_or_404(Task,pk=pk)
    tasks.is_completed=True
    tasks.save()
    return redirect('home')
def uncomplete_task(request,pk):
    tasks=get_object_or_404(Task,pk=pk)
    tasks.is_completed=False
    tasks.save()
    return redirect('home')
def edit_task(request,pk):
    gettasks=get_object_or_404(Task,pk=pk)
    if request.method=="POST":
        tasks=request.POST['task']
        gettasks.task=tasks
        gettasks.save()
        return redirect('home')
    else:
        context={
            'gettask':gettasks
        }
        return render(request,"edit_task.html",context)
def delete_task(request,pk):
    tasks=get_object_or_404(Task,pk=pk)
    tasks.delete()
    return redirect('home')

