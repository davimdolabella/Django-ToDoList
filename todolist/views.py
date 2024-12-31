from django.shortcuts import render

def home(request):
    return render(request, 'todolist/pages/home.html', {
        'range':range(10),
    })
