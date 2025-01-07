from django import forms
from todolist.models import Task
from utils.django_forms import add_placeholder
class TaskForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        add_placeholder(self.fields['title'], 'Your task title'),
        add_placeholder(self.fields['description'], 'Your task description'),
    class Meta:
        model = Task
        fields = [
            'title',
            'description',
            'deadline',
        ]