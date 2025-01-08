from django.urls import reverse
from .base import BaseTodolistViewTest
class DetailViewTestCase(BaseTodolistViewTest):
    
    def test_detail_page_status_code_404_if_wrong_task_id(self):
        self.client.login(username='testuser', password='password')
        response = self.client.get(reverse('todolist:detail',args=[50]))
        self.assertEqual(response.status_code, 404)
    
    def test_detail_use_correct_template(self):
        self.client.login(username='testuser', password='password')
        response = self.client.get(reverse('todolist:detail',args=[1]))
        self.assertTemplateUsed(response, 'todolist/pages/home.html')
