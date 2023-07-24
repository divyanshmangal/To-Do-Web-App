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

