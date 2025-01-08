from django.urls import reverse
from .base import BaseTodolistViewTest
class RegisterTaskViewTestCase(BaseTodolistViewTest):
    def test_register_task_view_status_code(self):
        self.client.login(username='testuser', password='password')
        response = self.client.get(reverse('todolist:register_task'))
        self.assertEqual(response.status_code, 200)

    def test_register_task_view_renders_template(self):
        self.client.login(username='testuser', password='password')
        response = self.client.get(reverse('todolist:register_task'))
        self.assertTemplateUsed(response, 'todolist/pages/register_task.html')

    def test_register_task_view_loads_empty_form(self):
        self.client.login(username='testuser', password='password')
        response = self.client.get(reverse('todolist:register_task'))
        self.assertIn('form', response.context)
        form = response.context['form']
        self.assertFalse(form.is_bound) 
        