from django.urls import reverse
from .base import BaseTodolistViewTest
from todolist.models import Task

class RegisterTaskCreateViewTestCase(BaseTodolistViewTest):
    def test_register_task_create_redirects_on_invalid_post(self):
        self.client.login(username='testuser', password='password')
        response = self.client.post(reverse('todolist:register_task_create'), {})
        self.assertRedirects(response, reverse('todolist:register_task'))

    def test_register_task_status_404_if_method_get(self):
        self.client.login(username='testuser', password='password')
        response = self.client.get(reverse('todolist:register_task_create'))
        self.assertEqual(response.status_code, 404)

    def test_register_task_create_creates_task_and_redirects(self):
        self.client.login(username='testuser', password='password')
        data = {
            'title': 'New Task',
            'description': 'Task description',
            'deadline': '2025-01-10',
        }
        response = self.client.post(reverse('todolist:register_task_create'), data)
        self.assertRedirects(response, reverse('todolist:home'))
        self.assertTrue(Task.objects.filter(title='New Task', author=self.user).exists())
