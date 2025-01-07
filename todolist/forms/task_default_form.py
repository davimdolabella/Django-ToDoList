from django import forms
from todolist.models import Task
from utils.django_forms import add_placeholder
from datetime import date
class TaskForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        add_placeholder(self.fields['title'], 'Your task title'),
        add_placeholder(self.fields['description'], 'Your task description'),
    title = forms.CharField(
        label='Task title',
        error_messages={
            'required':'Task title is required',
            'max_length':'Task Title must have less than 25 characters',
            'min_length':'Task Title must have at least 4 characters',
        },
        max_length=25,min_length=4
    )
    description = forms.CharField(
        widget=forms.Textarea(),
        label='Task Description',
        error_messages={
            'required':'Task description is required',
            'max_length':'Task description must have less than 500 characters',
            'min_length':'Task description must have at least 4 characters',
        },
        max_length=500,min_length=4
    )
    deadline = forms.DateField(
        widget=forms.DateInput(
            attrs={
                'type':'date',
                'class':'date-input',
                'min':date.today(),
                'required':True,
            }
        ),
        label='Deadline',
        initial=date.today(),
        error_messages={'required':'Task Deadline is required'}
    )
    class Meta:
        model = Task
        fields = [
            'title',
            'description',
            'deadline',
        ]