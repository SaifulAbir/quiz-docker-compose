# Generated by Django 4.1.3 on 2023-01-11 10:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tournament', '0002_remove_tournament_question_tournament_question'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tournament',
            name='question',
        ),
        migrations.AddField(
            model_name='tournament',
            name='banner',
            field=models.ImageField(default=1, upload_to=''),
            preserve_default=False,
        ),
    ]