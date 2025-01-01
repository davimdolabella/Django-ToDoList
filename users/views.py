from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import Http404
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .forms import LoginForm
from django.contrib.auth.decorators import login_required

def register_view(request):
    return render(request, 'users/pages/home.html')

def register_create(request):
    return render(request, 'users/pages/home.html')

def login_view(request):
    if request.user.is_authenticated:
        return redirect('todolist:home')
    else:
        form = LoginForm()
        form_action = reverse('users:login_create')
        return render(request, 'users/pages/login.html',{
            'form': form,
            'form_action': form_action
        })

def login_create(request):
    if not request.POST:
        raise Http404()
    form = LoginForm(request.POST)

    if form.is_valid():
        authenticated_user = authenticate(
            username=form.cleaned_data.get('username', ''),
            password=form.cleaned_data.get('password', '')
        )

        if authenticated_user is not None:
            messages.success(request, 'You are logged in!')
            login(request, authenticated_user)
        else:
            messages.error(request, 'Invalid credentials')
        

    else:
        messages.error(request, 'Invalid username or password')
    return redirect('users:login')
    

@login_required(login_url='users:login', redirect_field_name='next')
def logout_view(request):
    if not request.POST:
        return redirect(reverse('users:login'))
    logout(request)
    messages.success(request, 'You are logged out!') 
    return redirect(reverse('users:login'))