from django.urls import path
from . import views
app_name = 'todolist'

urlpatterns = [
     path('', views.home, name='home'),
     path('detail/<int:task_id>/', views.detail, name='detail'),
     path('todolist/search/', views.search, name="search"),
     path('todolist/check/<int:task_id>/', views.check_item_view, name="check_item"),
]
