# Generated by Django 5.1.4 on 2025-01-06 21:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todolist', '0002_alter_task_title'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='slug',
        ),
    ]
