from django.urls import path
from . import views
app_name = 'todolist'

urlpatterns = [
     path('', views.home, name='home')
]
