from django.test import TestCase
from django.contrib.auth.models import User
from todolist.models import Task
from datetime import date
from django.core.exceptions import ValidationError

class TaskModelTestCase(TestCase):
    def setUp(self):
        # Cria um usuário fictício para associar a tarefa
        self.user = User.objects.create_user(username="testuser", password="password")
        
        # Cria uma instância de Task
        self.task = Task.objects.create(
            title="Buy milk",
            description="Go to supermarket and buy milk.",
            deadline=date.today(),
            author=self.user
        )

    def test_task_str(self):
        self.assertEqual(str(self.task), "Buy milk")

    def test_task_title_max_lenght(self):
        self.task.title = 'a' * 36
        with self.assertRaises(ValidationError):
            self.task.full_clean()

    def test_task_is_past_deadline(self):
        self.task.deadline = date(2000,10,10)
        past = self.task.is_past_deadline
        self.assertEqual(past, True)
        self.task.deadline = date.today()
        not_past = self.task.is_past_deadline
        self.assertEqual(not_past, False)