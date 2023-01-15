# Generated by Django 4.1.3 on 2023-01-11 06:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('question', '0007_categorywiseleaderboard_user_name_and_more'),
        ('tournament', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tournament',
            name='question',
        ),
        migrations.AddField(
            model_name='tournament',
            name='question',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, related_name='questions', to='question.question'),
            preserve_default=False,
        ),
    ]