# Generated by Django 4.1.3 on 2022-11-23 08:08

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('projects', '0005_project_owner'),
        ('users', '0002_profiles_username'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Profiles',
            new_name='Profile',
        ),
    ]
