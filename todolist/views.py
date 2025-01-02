from django.shortcuts import render, redirect, get_object_or_404
from .models import Task
from django.contrib.auth.decorators import login_required


@login_required(login_url='users:login', redirect_field_name='next')
def home(request):
    tasks = Task.objects.filter(
            author=request.user
        ).order_by('-id')
    return render(request, 'todolist/pages/home.html', {
        'tasks':tasks,
    })

@login_required(login_url='users:login', redirect_field_name='next')
def detail(request, task_id):
    task = get_object_or_404(Task, pk=task_id)
    return render(request, 'todolist/pages/home.html', {
        'task':task,
        'is_detail_page':True,
    })