from django.test import TestCase
from users.forms import LoginForm

class TaskFormTestCase(TestCase):
    def test_placeholders(self):
        form = LoginForm()

        username_placeholder = form.fields['username'].widget.attrs.get('placeholder')
        self.assertEqual(username_placeholder, 'Type your username')

        password_placeholder = form.fields['password'].widget.attrs.get('placeholder')
        self.assertEqual(password_placeholder, 'Type your password')