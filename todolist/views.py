from django.shortcuts import render, redirect
from .models import Task
from django.contrib.auth.decorators import login_required

@login_required(login_url='users:login', redirect_field_name='next')
def home(request):
    tasks = Task.objects.filter(
            author=request.user
        ).order_by('-id')
    return render(request, 'todolist/pages/home.html', {
        'tasks':tasks,
        'title':'a' *20
    })
