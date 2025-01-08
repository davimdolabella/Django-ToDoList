from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from .base import BaseTodolistViewTest

class HomeTest(BaseTodolistViewTest):
    def test_home_return_status_code_302_if_url_is_ok_and_if_no_login(self):
        response = self.client.get(reverse('todolist:home'))
        self.assertEqual(response.status_code, 302)

    def test_home_return_status_code_200_if_url_is_ok_and_if_login(self):
        self.client.login(username='testuser', password='password')
        response = self.client.get(reverse('todolist:home'))
        self.assertEqual(response.status_code, 200)
    
    def test_home_use_correct_template(self):
        self.client.login(username='testuser', password='password')
        response = self.client.get(reverse('todolist:home'))
        self.assertTemplateUsed(response, 'todolist/pages/home.html')

    def test_home_shows_create_task_if_no_task(self):
        User.objects.create_user(username='test_user_no_task', password='Tset1234')
        self.client.login(username='test_user_no_task', password='Tset1234')
        response = self.client.get(reverse('todolist:home'))
        self.assertIn('No task found here 😥', response.content.decode())