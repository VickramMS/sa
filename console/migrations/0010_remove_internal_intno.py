# Generated by Django 2.2 on 2019-12-04 17:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('console', '0009_auto_20191204_2253'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='internal',
            name='intno',
        ),
    ]
