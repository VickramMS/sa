# Generated by Django 2.2 on 2019-06-21 05:02

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('users', '0009_auto_20190621_1024'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Student',
            new_name='Profile',
        ),
    ]