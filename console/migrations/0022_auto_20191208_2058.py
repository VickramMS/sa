# Generated by Django 2.2 on 2019-12-08 15:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('console', '0021_auto_20191206_2316'),
    ]

    operations = [
        migrations.AlterField(
            model_name='grade',
            name='letter',
            field=models.CharField(max_length=1, unique=True),
        ),
        migrations.AlterField(
            model_name='internal',
            name='marks',
            field=models.CharField(default=100, max_length=3),
        ),
        migrations.AlterField(
            model_name='internal',
            name='marks1',
            field=models.CharField(default=0, max_length=3),
        ),
        migrations.AlterField(
            model_name='internal',
            name='marks2',
            field=models.CharField(default=0, max_length=3),
        ),
        migrations.AlterField(
            model_name='internal',
            name='marks3',
            field=models.CharField(default=0, max_length=3),
        ),
        migrations.AlterField(
            model_name='internal',
            name='marksob',
            field=models.CharField(default=0, max_length=3),
        ),
        migrations.AlterField(
            model_name='subject',
            name='subcode',
            field=models.CharField(max_length=7, unique=True),
        ),
    ]