from django.db import models
from django.contrib.auth.models import User
import datetime

class Task(models.Model):
    def __str__(self):
        return self.title
    title = models.CharField(max_length=35)
    description = models.TextField(max_length=500)
    checked = models.BooleanField(default=False)
    deadline = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    slug = models.SlugField(max_length=20, unique=True)
    author = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True
    )

    def is_past_deadline(self):
        return datetime.date.today() > self.deadline
