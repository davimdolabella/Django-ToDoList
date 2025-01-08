from django.urls import reverse
from django.test import TestCase
from django.contrib.auth.models import User

class RegisterCreateViewTestCase(TestCase):
    def setUp(self):
        self.valid_data = {
            'username': 'testuser',
            'email': 'test@example.com',
            'first_name': 'Test',
            'last_name': 'User',
            'password': 'StrongPass123',
            'password2': 'StrongPass123',
        }
        self.invalid_data = {
            'username': '',
            'email': '',
            'first_name': '',
            'last_name': '',
            'password': '',
            'password2': '',
        }

    def test_register_create_redirects_to_login_on_success(self):
        response = self.client.post(reverse('users:register_create'), self.valid_data)
        self.assertRedirects(response, reverse('users:login'))
        self.assertTrue(User.objects.filter(username='testuser').exists())

    def test_register_create_stores_form_data_in_session_on_failure(self):
        response = self.client.post(reverse('users:register_create'), self.invalid_data)
        session = self.client.session
        self.assertIn('register_form_data', session)
        self.assertEqual(session['register_form_data'], self.invalid_data)

    def test_register_create_does_not_store_form_data_on_success(self):
        session = self.client.session
        session['register_form_data'] = {'username': 'old_data'}
        session.save()
        self.client.post(reverse('users:register_create'), self.valid_data)
        session = self.client.session
        self.assertNotIn('register_form_data', session)

    def test_register_create_raises_404_if_get_method(self):
        response = self.client.get(reverse('users:register_create'))
        self.assertEqual(response.status_code, 404)

    def test_register_create_redirects_back_to_register_on_failure(self):
        response = self.client.post(reverse('users:register_create'), self.invalid_data)
        self.assertRedirects(response, reverse('users:register'))

    def test_register_create_creates_user_on_success(self):
        self.client.post(reverse('users:register_create'), self.valid_data)
        user_exists = User.objects.filter(username='testuser').exists()
        self.assertTrue(user_exists)
