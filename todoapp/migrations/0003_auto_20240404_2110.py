# Generated by Django 3.2.12 on 2024-04-04 21:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todoapp', '0002_alter_task_time'),
    ]

    operations = [
        migrations.RenameField(
            model_name='task',
            old_name='complete',
            new_name='Complete',
        ),
        migrations.RenameField(
            model_name='task',
            old_name='title',
            new_name='Title',
        ),
    ]