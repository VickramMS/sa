# Generated by Django 2.2 on 2019-06-21 04:54

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('users', '0008_delete_attendance'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Profile',
            new_name='Student',
        ),
    ]