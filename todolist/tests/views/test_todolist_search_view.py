
from django.urls import reverse
from .base import BaseTodolistViewTest
class SearchViewTestCase(BaseTodolistViewTest):
    
    def test_search_view_search_function(self):
        self.client.login(username='testuser', password='password')
        response = self.client.get(reverse('todolist:search'), {'q': 'Searchable'})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.task1.title)
        self.assertNotContains(response, self.task2.title)

    def test_search_view_redirect_home_if_no_search_term(self):
        self.client.login(username='testuser', password='password')
        response = self.client.get(reverse('todolist:search'))
        self.assertRedirects(response, reverse('todolist:home'))