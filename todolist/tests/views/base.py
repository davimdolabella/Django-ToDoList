from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from todolist.models import Task
from datetime import date
class BaseTodolistViewTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='password')
        self.task1 = Task.objects.create(title='Searchable Task', description='Searchable Description', author=self.user, deadline=date.today(), checked=True)
        self.task2 = Task.objects.create(title='Another Task', description='Description 2', author=self.user, deadline=date.today())
