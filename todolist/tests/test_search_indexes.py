from django.test import TestCase
from haystack.query import SearchQuerySet
from todolist.models import Task
from todolist.search_indexes import TaskIndex  
from datetime import date

class TaskIndexTestCase(TestCase):
    def setUp(self):
        # Cria objetos Task para testar
        self.task1 = Task.objects.create(
            title="Buy food",
            description="Comprar ração para o cachorro",
            deadline=date.today()
        )
        self.task2 = Task.objects.create(
            title="Limpar a casa",
            description="I want to clean my house",
            deadline=date.today()
        )

        # Atualiza o índice manualmente (necessário para testes)
        from haystack.management.commands.update_index import Command
        Command().handle(interactive=False)

    def test_search_task_by_title(self):
        results = SearchQuerySet().filter(title="Buy food")
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0].object, self.task1)

    def test_search_task_by_description(self):
        results = SearchQuerySet().filter(description="I want to clean my house")
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0].object, self.task2)

    def test_search_with_partial_title(self):
        results = SearchQuerySet().autocomplete(text="Bu")
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0].object, self.task1)