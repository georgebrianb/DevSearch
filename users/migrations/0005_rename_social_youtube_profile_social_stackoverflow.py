# Generated by Django 4.0.1 on 2022-01-25 16:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_remove_skill_owner_profile_skills_skill_owners'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='social_youtube',
            new_name='social_stackoverflow',
        ),
    ]
