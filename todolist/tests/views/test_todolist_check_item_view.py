from django.urls import reverse
from .base import BaseTodolistViewTest
from todolist.models import Task
class CheckViewTestCase(BaseTodolistViewTest):
    
    def test_check_page_status_code_404_if_wrong_task_id(self):
        self.client.login(username='testuser', password='password')
        response = self.client.post(reverse('todolist:check_item', args=[3]))
        self.assertEqual(response.status_code, 404)
    
    def test_check_page_status_code_400_if_no_method_POST(self):
        self.client.login(username='testuser', password='password')
        response = self.client.get(reverse('todolist:check_item', args=[1]))
        self.assertEqual(response.status_code, 400)

    def test_check_page_check_and_uncheck_tasks(self):
        self.client.login(username='testuser', password='password')
        self.client.post(reverse('todolist:check_item', args=[self.task1.id]))
        self.task1.refresh_from_db()
        self.assertFalse(self.task1.checked)
        self.client.post(reverse('todolist:check_item', args=[self.task1.id]))
        self.task1.refresh_from_db()
        self.assertTrue(self.task1.checked)