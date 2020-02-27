# Generated by Django 3.0.3 on 2020-02-24 08:10

from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=30, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('user_type', models.CharField(choices=[('ADMIN', 'ADMIN'), ('HOD', 'HOD'), ('STAFF', 'STAFF'), ('REPRESENTATIVE', 'REPRESENTATIVE'), ('STUDENT', 'STUDENT')], max_length=20)),
                ('department', models.CharField(choices=[('MECH', 'Mechanical'), ('CIVIL', 'Civil'), ('EEE', 'Electrical and Electronics'), ('ECE', 'Electronics and Communication'), ('CSE', 'Computer Science and Engineering'), ('OTHER', 'Others')], max_length=20)),
                ('email', models.EmailField(max_length=254)),
                ('date_of_birth', models.DateField(blank=True, null=True)),
                ('age', models.IntegerField(blank=True, null=True)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.CharField(choices=[('First Year', 'First Year'), ('Second Year', 'Second Year'), ('Third Year', 'Third Year'), ('Fourth Year', 'Fourth Year'), ('Completed', 'Completed')], max_length=30)),
                ('roll_no', models.CharField(blank=True, max_length=7)),
                ('reg_no', models.CharField(blank=True, max_length=12)),
                ('avatar', models.ImageField(default='default.jpg', upload_to='media')),
                ('father', models.CharField(blank=True, max_length=50)),
                ('mother', models.CharField(blank=True, max_length=50)),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female'), ('Transgender', 'Transgender')], default='MALE', max_length=12)),
                ('address1', models.CharField(blank=True, max_length=50)),
                ('address2', models.CharField(blank=True, max_length=50)),
                ('address3', models.CharField(blank=True, max_length=50)),
                ('address4', models.CharField(blank=True, max_length=50)),
                ('city', models.CharField(blank=True, max_length=50)),
                ('state', models.CharField(choices=[('KA', 'Karnataka'), ('AP', 'Andhra Pradesh'), ('KL', 'Kerala'), ('TN', 'Tamil Nadu'), ('MH', 'Maharashtra'), ('UP', 'Uttar Pradesh'), ('GA', 'Goa'), ('GJ', 'Gujarat'), ('RJ', 'Rajasthan'), ('HP', 'Himachal Pradesh'), ('JK', 'Jammu and Kashmir'), ('TG', 'Telangana'), ('AR', 'Arunachal Pradesh'), ('AS', 'Assam'), ('BR', 'Bihar'), ('CG', 'Chattisgarh'), ('HR', 'Haryana'), ('JH', 'Jharkhand'), ('MP', 'Madhya Pradesh'), ('MN', 'Manipur'), ('ML', 'Meghalaya'), ('MZ', 'Mizoram'), ('NL', 'Nagaland'), ('OR', 'Orissa'), ('PB', 'Punjab'), ('SK', 'Sikkim'), ('TR', 'Tripura'), ('UA', 'Uttarakhand'), ('WB', 'West Bengal'), ('AN', 'Andaman and Nicobar'), ('CH', 'Chandigarh'), ('DN', 'Dadra and Nagar Haveli'), ('DD', 'Daman and Diu'), ('DL', 'Delhi'), ('LD', 'Lakshadweep'), ('PY', 'Pondicherry')], default='TN', max_length=30)),
                ('pincode', models.CharField(blank=True, max_length=6)),
                ('full_address', models.TextField(blank=True)),
                ('phone', models.CharField(blank=True, max_length=10)),
                ('father_mobile', models.CharField(blank=True, max_length=10)),
                ('mother_mobile', models.CharField(blank=True, max_length=10)),
                ('resident', models.CharField(choices=[('Days Scholar', 'Day Scholar'), ('Hostel', 'Hostel'), ('OTHER', 'Other')], default='Hostel', max_length=20)),
                ('transport', models.CharField(choices=[('Self Walk', 'Self Walk'), ('Self Vehicle', 'Self Vehicle'), ('Public Transport', 'Public Transport')], default='Self Walk', max_length=20)),
                ('blood', models.CharField(choices=[('A +ve', 'A +ve'), ('A -ve', 'A -ve'), ('B +ve', 'B +ve'), ('B -ve', 'B -ve'), ('O +ve', 'O +ve'), ('O -ve', 'O -ve'), ('AB +ve', 'AB +ve'), ('AB -ve', 'AB -ve'), ('Other', 'Other')], default='A +ve', max_length=10)),
                ('aadhar', models.CharField(max_length=12, null=True, unique=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Staff',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
