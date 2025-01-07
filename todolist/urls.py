from django.urls import path
from . import views
app_name = 'todolist'

urlpatterns = [
     path('', views.home, name='home'),
     path('detail/<int:task_id>/', views.detail, name='detail'),
     path('todolist/search/', views.search, name="search"),
     path('todolist/check/<int:task_id>/', views.check_item_view, name="check_item"),
     path('todolist/register/task/', views.register_task_view, name="register_task"),
     path('todolist/register/task/create', views.register_task_create, name="register_task_create"),
     path('todolist/edit/task/<int:task_id>/', views.edit_task_view, name="edit_task"),
     path('todolist/edit/task/create', views.edit_task_create, name="edit_task_create"),
]
