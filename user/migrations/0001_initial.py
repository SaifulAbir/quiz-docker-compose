# Generated by Django 4.1.3 on 2022-11-16 10:33

import django.core.validators
from django.db import migrations, models
import user.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='OTPModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('contact_number', models.CharField(max_length=20, verbose_name='Contact Number')),
                ('otp_number', models.IntegerField(verbose_name='OTP Number')),
                ('verified_phone', models.BooleanField(default=False)),
                ('expired_time', models.DateTimeField(verbose_name='Expired Time')),
            ],
            options={
                'verbose_name': 'OTPModel',
                'verbose_name_plural': 'OTPModels',
                'db_table': 'otp_models',
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('username', models.CharField(max_length=100, unique=True)),
                ('name', models.CharField(blank=True, max_length=150)),
                ('email', models.EmailField(max_length=255, unique=True)),
                ('is_active', models.BooleanField(default=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_superuser', models.BooleanField(default=False)),
                ('verified_email', models.BooleanField(default=False)),
                ('phone', models.CharField(blank=True, max_length=255, null=True, validators=[django.core.validators.RegexValidator(message='Invalid phone number', regex='^[+]*[(]{0,1}[0-9]{1,4}[)]{0,1}[-\\s\\./0-9]*$')])),
                ('date_joined', models.DateTimeField(auto_now_add=True, verbose_name='date joined')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'User',
                'verbose_name_plural': 'Users',
                'db_table': 'users',
                'ordering': ['-is_active'],
            },
            managers=[
                ('objects', user.models.UserManager()),
            ],
        ),
    ]
