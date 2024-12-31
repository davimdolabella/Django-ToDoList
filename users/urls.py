from django.urls import path
from users import views

app_name = 'users'

urlpatterns = [
    path('register/', views.register, name='register'),
    path('register/create/', views.register_create, name='register_create'),
    path('login/', views.login, name='login'),
    path('login/create/', views.login_create, name='login_create'),
    path('logout/', views.logout, name='logout'),
]
