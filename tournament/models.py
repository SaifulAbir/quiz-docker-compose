from django.db import models

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
    category = models.ForeignKey(Category, on_delete=models.CASCADE, blank=False, null=False)
    question = models.ManyToManyField(Question, blank=True)
    published = models.BooleanField(default=False)
    banner = models.ImageField()
    status = models.CharField(max_length=20, null=False, blank=False, choices=TOURNAMENT_STATUS, default=TOURNAMENT_STATUS[1][1])

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Tournament'
        verbose_name_plural = 'Tournaments'
        db_table = 'tournament'


# class TournamentQuestion(AbstractTimeStamp):
#     tournament = models.ForeignKey(Tournament, on_delete=models.PROTECT, null=False, blank=False)
#     question = models.ForeignKey(Question, on_delete=models.PROTECT, null=False, blank=False)