from django.shortcuts import render, redirect, get_object_or_404
from .models import Task
from django.contrib.auth.decorators import login_required
from django.http import Http404
from haystack.query import SearchQuerySet

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
@login_required(login_url='users:login', redirect_field_name='next')
def search(request):
    search_term = request.GET.get('q', '').strip()
    if search_term:
        tasks = SearchQuerySet().filter(content=search_term)
    else:
        raise Http404
    return render(request, 'todolist/pages/home.html', {
        'tasks':tasks,
        'search_term':search_term,
    })