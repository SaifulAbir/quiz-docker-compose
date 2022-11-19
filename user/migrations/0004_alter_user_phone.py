# Generated by Django 4.0 on 2022-11-18 14:47

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_rename_name_user_full_name_remove_user_username_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='phone',
            field=models.CharField(max_length=255, validators=[django.core.validators.RegexValidator(message='Invalid phone number', regex='^[+]*[(]{0,1}[0-9]{1,4}[)]{0,1}[-\\s\\./0-9]*$')]),
        ),
    ]
