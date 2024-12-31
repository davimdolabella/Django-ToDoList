from django.test import TestCase
from django.urls import reverse

class HomeTest(TestCase):
    def setUp(self):
        self.url = reverse('todolist:home')
        self.get_response = self.client.get(self.url)
        return super().setUp()
    def test_home_return_status_code_200_if_url_is_ok(self):
        self.assertEqual(self.get_response.status_code, 200)
    def test_home_use_correct_template(self):
        self.assertTemplateUsed(self.get_response, 'todolist/pages/home.html')
