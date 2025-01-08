from django.urls import reverse
from django.test import TestCase
from django.contrib.auth.models import User

class LoginViewTestCase(TestCase):
    def test_login_view_redirects_if_authenticated(self):
        user = User.objects.create_user(username='testuser', password='password')
        self.client.login(username='testuser', password='password')
        response = self.client.get(reverse('users:login'))
        self.assertRedirects(response, reverse('todolist:home'))

    def test_login_view_renders_login_page_if_not_authenticated(self):
        response = self.client.get(reverse('users:login'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'users/pages/login.html')
        self.assertIn('form', response.context)
