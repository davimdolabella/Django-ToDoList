from django.shortcuts import render

def register(request):
    return render(request, 'users/pages/home.html')

def register_create(request):
    return render(request, 'users/pages/home.html')

def login(request):
    return render(request, 'users/pages/home.html')

def login_create(request):
    return render(request, 'users/pages/home.html')

def logout(request):
    return render(request, 'users/pages/home.html')
