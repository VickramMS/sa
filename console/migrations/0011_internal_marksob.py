# Generated by Django 2.2 on 2019-12-04 17:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('console', '0010_remove_internal_intno'),
    ]

    operations = [
        migrations.AddField(
            model_name='internal',
            name='marksob',
            field=models.IntegerField(default=0),
        ),
    ]