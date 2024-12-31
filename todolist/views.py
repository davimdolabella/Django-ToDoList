from django.shortcuts import render
from .models import Task

def home(request):
    tasks = Task.objects.filter(
        author=request.user
    ).order_by('-id')
    return render(request, 'todolist/pages/home.html', {
        'tasks':tasks,
        'title':'a' *20
    })
