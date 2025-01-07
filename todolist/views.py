from django.shortcuts import render, redirect, get_object_or_404
from .models import Task
from django.contrib.auth.decorators import login_required
from django.http import Http404, JsonResponse
from haystack.query import SearchQuerySet
from django.contrib import messages

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
        search_tasks = SearchQuerySet().filter(content=search_term)
    else:
        return redirect('todolist:home')
    tasks = [task.object for task in search_tasks]
    
    return render(request, 'todolist/pages/home.html', {
        'tasks':tasks,
        'search_term':search_term,
        'is_search_page':True,
    })

@login_required(login_url='users:login', redirect_field_name='next')
def check_item_view(request, task_id):
    if request.method == 'POST':
        task = get_object_or_404(Task, pk=task_id, author=request.user)
        task.checked = not task.checked
        task.save()
        return JsonResponse({'is_checked': task.checked})
        
    return JsonResponse({'error': 'Invalid request method'}, status=400)

@login_required(login_url='users:login', redirect_field_name='next')
def register_task(request):
    return ('users:login')
@login_required(login_url='users:login', redirect_field_name='next')
def register_task_create(request):
    return ('users:login')