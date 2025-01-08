from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse 
from .models import Task
from django.contrib.auth.decorators import login_required
from .forms import TaskForm
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
    tasks = []
    this_author_tasks = []
    if search_term:
        search_tasks = SearchQuerySet().filter(content=search_term)
        if search_tasks:
            tasks = [task.object for task in search_tasks]
            this_author_tasks = []
            for task in tasks:
                if task and task.author and task.author == request.user:  # Verifica se `task.author` existe
                    this_author_tasks.append(task)
    else:
        return redirect('todolist:home')


    return render(request, 'todolist/pages/home.html', {
        'tasks':this_author_tasks,
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
def delete_item_view(request, task_id):
    if request.method == 'POST':
        task = get_object_or_404(Task, pk=task_id, author=request.user)
        messages.success(request, f"Task '{task.title}' deleted successfully!")
        task.delete()
        return redirect('todolist:home')
    raise Http404

@login_required(login_url='users:login', redirect_field_name='next')
def register_task_view(request):
    task_form_data = request.session.get('task_form_data', None)
    form = TaskForm(task_form_data)
    form_action = reverse('todolist:register_task_create')
    request.session.pop('task_form_data', None)
    return render(request, 'todolist/pages/register_task.html',{
        'form':form,
        'form_action':form_action,
        'is_task_form':True,
    })

@login_required(login_url='users:login', redirect_field_name='next')
def register_task_create(request):
    if request.method == 'POST':
        POST = request.POST
        request.session['task_form_data'] = POST
        form = TaskForm(request.POST)
        if form.is_valid():
            user = request.user
            task = form.save(commit=False)
            task.author = user
            task.save()
            messages.success(request, f"Task '{task.title}' created successfully!")
            del(request.session['task_form_data'])
            return redirect('todolist:home')
        return redirect('todolist:register_task')
    raise Http404
    

@login_required(login_url='users:login', redirect_field_name='next')
def edit_task_view(request, task_id):
    task_edit_form_data = request.session.get('task_edit_form_data', None)
    task = Task.objects.get(pk=task_id, author=request.user)  
    form = TaskForm(task_edit_form_data, instance=task)
    form_action = reverse('todolist:edit_task_create', kwargs={'task_id': task_id})
    return render(request, 'todolist/pages/edit_task.html',{
        'form':form,
        'form_action':form_action,
        'is_task_form':True,
        'task':task,
    })


@login_required(login_url='users:login', redirect_field_name='next')
def edit_task_create(request, task_id):
    if request.method == 'POST':
        POST = request.POST
        request.session['task_edit_form_data'] = POST
        task = Task.objects.get(pk=task_id, author=request.user)
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            updated_task = form.save()
            print(updated_task.title)
            messages.success(request, f"Task '{updated_task.title}' edited successfully!")
            del(request.session['task_edit_form_data'])
            return redirect('todolist:home')
        return redirect('todolist:edit_task', task_id=task_id)
    raise Http404
