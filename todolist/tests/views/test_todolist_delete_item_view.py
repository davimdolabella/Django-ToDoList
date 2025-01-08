from django.urls import reverse
from .base import BaseTodolistViewTest
from todolist.models import Task
from datetime import date
class DeleteViewTestCase(BaseTodolistViewTest):
    
    def test_delete_page_status_code_404_if_wrong_task_id(self):
        self.client.login(username='testuser', password='password')
        response = self.client.post(reverse('todolist:delete_item', args=[3]))
        self.assertEqual(response.status_code, 404)
    
    def test_delete_page_status_code_404_if_no_method_POST(self):
        self.client.login(username='testuser', password='password')
        response = self.client.get(reverse('todolist:delete_item', args=[1]))
        self.assertEqual(response.status_code, 404)

    def test_delete_view_delete_tasks(self):
        
        self.client.login(username='testuser', password='password')
        
        task3 = Task.objects.create(title='Another Task', description='Description 2', deadline=date.today(), author=self.user)
        task_id = task3.pk
        response = self.client.post(reverse('todolist:delete_item', args=[task_id]))
        self.assertEqual(response.status_code, 302)
        self.assertFalse(Task.objects.filter(pk=task_id).exists())
        