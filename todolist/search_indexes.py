from haystack import indexes
from .models import Task
from haystack.fields import EdgeNgramField

class TaskIndex(indexes.SearchIndex, indexes.Indexable):
    text = EdgeNgramField(document=True, use_template=True)
    title = indexes.CharField(model_attr='title')
    description = indexes.CharField(model_attr='description')

    def get_model(self):
        return Task

    def index_queryset(self, using=None):
        return self.get_model().objects.all()