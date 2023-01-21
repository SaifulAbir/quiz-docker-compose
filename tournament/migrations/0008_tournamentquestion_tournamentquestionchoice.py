# Generated by Django 4.1.3 on 2023-01-21 09:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tournament', '0007_alter_tournament_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='TournamentQuestion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=1000)),
                ('tournament', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='tournament.tournament')),
            ],
            options={
                'verbose_name': 'TournamentQuestion',
                'verbose_name_plural': 'TournamentQuestions',
                'db_table': 'tour_question',
            },
        ),
        migrations.CreateModel(
            name='TournamentQuestionChoice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=500)),
                ('is_answer', models.BooleanField()),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='tournament_question_choice', to='tournament.tournamentquestion')),
            ],
            options={
                'verbose_name': 'TournamentQuestionChoice',
                'verbose_name_plural': 'TournamentQuestionChoices',
                'db_table': 'tournament_question_choice',
            },
        ),
    ]