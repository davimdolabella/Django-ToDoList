from django.test import TestCase
from todolist.forms import TaskForm

class TaskFormTestCase(TestCase):
    def test_placeholders(self):
        form = TaskForm()

        title_placeholder = form.fields['title'].widget.attrs.get('placeholder')
        self.assertEqual(title_placeholder, 'Your task title')

        description_placeholder = form.fields['description'].widget.attrs.get('placeholder')
        self.assertEqual(description_placeholder, 'Your task description')