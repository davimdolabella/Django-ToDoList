from django.urls import reverse
from .base import BaseTodolistViewTest
from todolist.models import Task

class EditTaskCreateViewTestCase(BaseTodolistViewTest):
    def test_edit_task_create_view_status_code_302_if_valid(self):
        self.client.login(username='testuser', password='password')
        valid_data = {
            'title': 'Updated Task Title',
            'description': 'Updated Description',
            'deadline': '2025-01-15',
        }
        response = self.client.post(reverse('todolist:edit_task_create', args=[self.task1.id]), valid_data)
        self.assertEqual(response.status_code, 302)
    def test_edit_task_create_status_code_404_if_get_method(self):
        self.client.login(username='testuser', password='password')
        valid_data = {
            'title': 'Updated Task Title',
            'description': 'Updated Description',
            'deadline': '2025-01-15',
        }
        response = self.client.get(reverse('todolist:edit_task_create', args=[self.task1.id]), valid_data)
        self.assertEqual(response.status_code, 404)

    def test_edit_task_create_view_redirects_to_home_on_valid_edit(self):
        self.client.login(username='testuser', password='password')
        valid_data = {
            'title': 'Updated Task Title',
            'description': 'Updated Description',
            'deadline': '2025-01-15',
        }
        response = self.client.post(reverse('todolist:edit_task_create', args=[self.task1.id]), valid_data)
        self.assertRedirects(response, reverse('todolist:home'))

    def test_edit_task_create_updates_task_in_database(self):
        self.client.login(username='testuser', password='password')
        valid_data = {
            'title': 'Updated Task Title',
            'description': 'Updated Description',
            'deadline': '2025-01-15',
        }
        self.client.post(reverse('todolist:edit_task_create', args=[self.task1.id]), valid_data)
        self.task1.refresh_from_db()
        self.assertEqual(self.task1.title, valid_data['title'])
        self.assertEqual(self.task1.description, valid_data['description'])
        self.assertEqual(str(self.task1.deadline), valid_data['deadline'])

    def test_edit_task_create_view_status_404_on_invalid_edit(self):
        self.client.login(username='testuser', password='password')
        invalid_data = {
            'title': '',
            'description': 'Updated Description',
            'deadline': '2025-01-15',
        }
        response = self.client.post(reverse('todolist:edit_task_create', args=[self.task1.id]), invalid_data)
        self.assertEqual(response.status_code, 302)

    def test_edit_task_create_redirects_to_edit_page_on_invalid_edit(self):
        self.client.login(username='testuser', password='password')
        invalid_data = {
            'title': '',
            'description': 'Updated Description',
            'deadline': '2025-01-15',
        }
        response = self.client.post(reverse('todolist:edit_task_create', args=[self.task1.id]), invalid_data)
        self.assertRedirects(response, reverse('todolist:edit_task', args=[self.task1.id]))

    def test_edit_task_create_does_not_update_task_on_invalid_edit(self):
        self.client.login(username='testuser', password='password')
        invalid_data = {
            'title': '',
            'description': 'Updated Description',
            'deadline': '2025-01-15',
        }
        self.client.post(reverse('todolist:edit_task_create', args=[self.task1.id]), invalid_data)
        self.task1.refresh_from_db()
        self.assertNotEqual(self.task1.title, invalid_data['title'])

    def test_edit_task_create_stores_form_data_in_session_on_invalid_edit(self):
        self.client.login(username='testuser', password='password')
        invalid_data = {
            'title': '',
            'description': 'Updated Description',
            'deadline': '2025-01-15',
        }
        response = self.client.post(reverse('todolist:edit_task_create', args=[self.task1.id]), invalid_data)
        session = self.client.session
        self.assertIn('task_edit_form_data', session)
        self.assertEqual(session['task_edit_form_data'], invalid_data)

    def test_edit_task_create_clears_session_on_valid_edit(self):
        self.client.login(username='testuser', password='password')
        valid_data = {
            'title': 'Updated Task Title',
            'description': 'Updated Description',
            'deadline': '2025-01-15',
        }
        session = self.client.session
        session['task_edit_form_data'] = {'title': 'Old Data'}
        session.save()
        self.client.post(reverse('todolist:edit_task_create', args=[self.task1.id]), valid_data)
        session = self.client.session
        self.assertNotIn('task_edit_form_data', session)
