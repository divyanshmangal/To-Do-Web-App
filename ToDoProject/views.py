from django.http import HttpResponse
from django.shortcuts import render
from todo.models import Task
def home(request):
    tasks=Task.objects.filter(is_completed=False).order_by('-update_at')
    is_completed=Task.objects.filter(is_completed=True)
    context={
        'task12':tasks,
        'complete':is_completed
    }
    return render(request,"home.html",context)