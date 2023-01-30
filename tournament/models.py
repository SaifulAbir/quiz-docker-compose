from django.db import models
from user.models import User

from quiz.models import AbstractTimeStamp
from question.models import Question, Category


# Create your models here.

class Tournament(AbstractTimeStamp):
    TOURNAMENT_STATUS = [
        ('DRAFT', 'Draft'),
        ('LIVE', 'Live'),
        ('CLOSED', 'Closed'),
    ]
    title = models.CharField(max_length=245, blank=False, null=False)
    description = models.TextField(blank=True, null=True)
    published = models.BooleanField(default=False)
    banner = models.ImageField()
    status = models.CharField(max_length=20, null=False, blank=False, choices=TOURNAMENT_STATUS, default=TOURNAMENT_STATUS[1][1])
    # start_date = models.DateTimeField()
    # end_date = models.DateTimeField()

    def __str__(self):
        return self.title

    class Meta:
        # ordering = ['-created_at']
        verbose_name = 'Tournament'
        verbose_name_plural = 'Tournaments'
        db_table = 'tournament'


class TournamentQuestion(AbstractTimeStamp):
    title = models.CharField(max_length=1000, null=False, blank=False)
    tournament = models.ForeignKey(Tournament, on_delete=models.PROTECT, blank=False, null=False)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "TournamentQuestion"
        verbose_name_plural = "TournamentQuestions"
        db_table = 'tour_question'


class TournamentQuestionChoice(AbstractTimeStamp):
    title = models.CharField(max_length=500, null=False, blank=False)
    question = models.ForeignKey(
        TournamentQuestion, on_delete=models.PROTECT, related_name='tournament_question_choice', blank=False, null=False)
    is_answer = models.BooleanField(null=False, blank=False)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "TournamentQuestionChoice"
        verbose_name_plural = "TournamentQuestionChoices"
        db_table = 'tournament_question_choice'


class StoreTournamentAnswer(AbstractTimeStamp):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    tournament_id = models.ForeignKey(Tournament, on_delete=models.CASCADE)
    point = models.IntegerField(null=False, blank=False, default='0')

    def __str__(self):
        return self.tournament_id.title

    class Meta:
        verbose_name = "StoreTournamentAnswer"
        verbose_name_plural = "StoreTournamentAnswers"
        db_table = 'store_tournament_answer'


class TournamentWiseLeaderBoard(AbstractTimeStamp):
    user_id = models.CharField(max_length=255, null=True, blank=True)
    tournament_id = models.CharField(max_length=255, null=True, blank=True)
    tour_point = models.IntegerField(null=True, blank=True, default='0')
    user_name = models.CharField(max_length=255, default='User Name')

    def __str__(self):
        return self.user_name

    class Meta:
        verbose_name = "TournamentWiseLeaderBoard"
        verbose_name_plural = "TournamentWiseLeaderBoards"
        db_table = 'tournament_wise_leader_board'
