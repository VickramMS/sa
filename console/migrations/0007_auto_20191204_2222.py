# Generated by Django 2.2 on 2019-12-04 16:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('console', '0006_auto_20191204_2118'),
    ]

    operations = [
        migrations.AlterField(
            model_name='semester',
            name='marksob',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='semester',
            name='markstot',
            field=models.IntegerField(default=100),
        ),
        migrations.CreateModel(
            name='internals',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('marksob', models.IntegerField(default=0)),
                ('marks', models.IntegerField(default=100)),
                ('intno', models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3')], default='1', max_length=1)),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='console.Subject')),
            ],
        ),
    ]
