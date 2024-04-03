# Generated by Django 5.0.1 on 2024-03-20 12:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='task',
            old_name='title',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='task',
            old_name='completed',
            new_name='status',
        ),
        migrations.RemoveField(
            model_name='task',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='task',
            name='description',
        ),
    ]