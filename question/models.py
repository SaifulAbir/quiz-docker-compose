from django.db import models
from django.utils import timezone

from quiz.models import AbstractTimeStamp
from user.models import User


class Category(AbstractTimeStamp):
    title = models.CharField(max_length=500, null=False, blank=False)
    created_at = models.DateTimeField(null=True, blank=True, default=timezone.now)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"
        db_table = 'category'


class Question(AbstractTimeStamp):
    title = models.CharField(max_length=1000, null=False, blank=False)
    category = models.ForeignKey(Category, on_delete=models.PROTECT, blank=False, null=False)
    level = models.CharField(max_length=255, null=False, blank=False)
    created_at = models.DateTimeField(null=True, blank=True, default=timezone.now)
    # hint = models.CharField()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Question"
        verbose_name_plural = "Questions"
        db_table = 'question'


class QuestionChoice(AbstractTimeStamp):
    title = models.CharField(max_length=500, null=False, blank=False)
    question = models.ForeignKey(
        Question, on_delete=models.PROTECT, related_name='question_choice', blank=False, null=False)
    is_answer = models.BooleanField(null=False, blank=False)
    created_at = models.DateTimeField(null=True, blank=True, default=timezone.now)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "QuestionChoice"
        verbose_name_plural = "QuestionChoices"
        db_table = 'question_choice'


class StoreAnswer(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    question_id = models.ForeignKey(Question, on_delete=models.CASCADE)
    created_at = models.DateTimeField(null=True, blank=True, default=timezone.now)
    answer = models.CharField(max_length=900, null=False, blank=False)

    def __str__(self):
        return self.user_id

    class Meta:
        verbose_name = "StoreAnswer"
        verbose_name_plural = "StoreAnswers"
        db_table = 'store_answer'

# class ParticipantAnswer(AbstractTimeStamp):



