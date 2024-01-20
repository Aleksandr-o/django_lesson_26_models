# Generated by Django 5.0.1 on 2024-01-20 14:32

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subtask',
            name='task',
            field=models.ForeignKey(limit_choices_to={'satus': 1}, on_delete=django.db.models.deletion.CASCADE, related_name='subtasks', to='todo.task'),
        ),
    ]
