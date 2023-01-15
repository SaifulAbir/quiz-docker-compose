# Generated by Django 4.1.3 on 2023-01-11 06:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('question', '0007_categorywiseleaderboard_user_name_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tournament',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=245)),
                ('description', models.TextField(blank=True, null=True)),
                ('published', models.BooleanField(default=False)),
                ('question', models.ManyToManyField(related_name='questions', to='question.question')),
            ],
            options={
                'verbose_name': 'Tournament',
                'verbose_name_plural': 'Tournaments',
                'db_table': 'tournament',
                'ordering': ['-created_at'],
            },
        ),
    ]