# Generated by Django 4.0.1 on 2022-01-18 15:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0002_project_test'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='test',
        ),
    ]
