# Generated by Django 3.2.12 on 2022-07-05 06:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todos', '0002_rename_status_todo_is_completed'),
    ]

    operations = [
        migrations.RenameField(
            model_name='todo',
            old_name='user',
            new_name='owner',
        ),
    ]