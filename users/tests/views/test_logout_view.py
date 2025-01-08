from django.urls import reverse
from django.test import TestCase
from django.contrib.auth.models import User

class LogoutViewTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='password123')

    def test_logout_view_redirects_to_login_on_get(self):
        self.client.login(username='testuser', password='password123')
        response = self.client.get(reverse('users:logout'), follow=True)
        self.assertRedirects(response, reverse('todolist:home'))

    def test_logout_view_logs_out_user_on_post(self):
        self.client.login(username='testuser', password='password123')
        response = self.client.post(reverse('users:logout'))
        self.assertRedirects(response, reverse('users:login'))
        messages = list(response.wsgi_request._messages)
        self.assertEqual(messages[0].message, 'You are logged out!')

