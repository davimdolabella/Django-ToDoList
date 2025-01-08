from django.urls import reverse
from django.test import TestCase
from django.contrib.auth.models import User
from django.http import Http404

class LoginCreateViewTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='Password123')

    def test_login_create_raises_404_on_get(self):
        response = self.client.get(reverse('users:login_create'))
        self.assertEqual(response.status_code, 404)
            

    def test_login_create_logs_in_user_on_valid_credentials(self):
        data = {
            'username': 'testuser',
            'password': 'Password123',
        }
        response = self.client.post(reverse('users:login_create'), data, follow=True)
        messages = list(response.wsgi_request._messages)
        self.assertEqual(messages[0].message, 'You are logged in!')

    def test_login_create_shows_error_on_invalid_credentials(self):
        data = {
            'username': 'testuser',
            'password': 'wrongpassword',
        }
        response = self.client.post(reverse('users:login_create'), data)
        self.assertRedirects(response, reverse('users:login'))
        messages = list(response.wsgi_request._messages)
        self.assertEqual(messages[0].message, 'Invalid credentials')

    def test_login_create_shows_error_on_invalid_form(self):
        data = {
            'username': '',
            'password': 'Password123',
        }
        response = self.client.post(reverse('users:login_create'), data)
        self.assertRedirects(response, reverse('users:login'))
        messages = list(response.wsgi_request._messages)
        self.assertEqual(messages[0].message, 'Invalid username or password')
