from django.urls import reverse
from .base import BaseTodolistViewTest
class EditTaskViewTestCase(BaseTodolistViewTest):
    def test_edit_task_view_status_code(self):
        self.client.login(username='testuser', password='password')
        response = self.client.get(reverse('todolist:edit_task',args=[self.task1.id]))
        self.assertEqual(response.status_code, 200)

    def test_edit_task_view_renders_template(self):
        self.client.login(username='testuser', password='password')
        response = self.client.get(reverse('todolist:edit_task',args=[self.task1.id]))
        self.assertTemplateUsed(response, 'todolist/pages/edit_task.html')

    def test_edit_task_view_loads_form_if_task1_data(self):
        self.client.login(username='testuser', password='password')
        response = self.client.get(reverse('todolist:edit_task', args=[self.task1.id]))
        self.assertIn('form', response.context)
        form = response.context['form']
        self.assertEqual(form.instance, self.task1)
        