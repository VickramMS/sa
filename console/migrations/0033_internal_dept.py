# Generated by Django 2.2 on 2019-12-09 04:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('console', '0032_auto_20191209_0853'),
    ]

    operations = [
        migrations.AddField(
            model_name='internal',
            name='dept',
            field=models.CharField(choices=[('MECH', 'Mechanical'), ('CIVIL', 'Civil'), ('EEE', 'Electrical and Electronics'), ('ECE', 'Electronics and Communication'), ('CSE', 'Computer Science and Engineering'), ('OTHER', 'Others')], default='MECH', max_length=5),
        ),
    ]