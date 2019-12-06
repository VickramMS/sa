# Generated by Django 2.2 on 2019-06-21 10:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('users', '0017_auto_20190621_1540'),
    ]

    operations = [
        migrations.CreateModel(
            name='Attendancee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Hour', models.CharField(blank=True, help_text='Hour', max_length=1)),
                ('subject', models.CharField(blank=True, help_text='Subject', max_length=8)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('presence', models.BooleanField(default=False)),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.DeleteModel(
            name='Attendance',
        ),
    ]
