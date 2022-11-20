# Generated by Django 4.0 on 2022-11-19 06:05

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0005_alter_user_email_alter_user_gender'),
    ]

    operations = [
        migrations.AlterField(
            model_name='otpmodel',
            name='contact_number',
            field=models.CharField(max_length=255, validators=[django.core.validators.RegexValidator(message='Invalid phone number', regex='^[+]*[(]{0,1}[0-9]{1,4}[)]{0,1}[-\\s\\./0-9]*$')], verbose_name='Contact Number'),
        ),
    ]