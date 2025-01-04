from django.urls import path
from . import views
app_name = 'todolist'

urlpatterns = [
     path('', views.home, name='home'),
     path('detail/<int:task_id>/', views.detail, name='detail'),
     path('recipes/search/', views.search, name="search"),
]
