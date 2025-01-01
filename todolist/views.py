from django.shortcuts import render, redirect
from .models import Task

def home(request):
    if request.user.is_authenticated:
        tasks = Task.objects.filter(
            author=request.user
        ).order_by('-id')
    else:
        tasks = None
        return redirect('users:login')
    
    
    return render(request, 'todolist/pages/home.html', {
        'tasks':tasks,
        'title':'a' *20
    })
