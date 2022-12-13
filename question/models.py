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
    cat_id = models.ForeignKey(Category, on_delete=models.CASCADE)
    point = models.IntegerField(null=False, blank=False, default='0')
    created_at = models.DateTimeField(null=True, blank=True, default=timezone.now)

    def __str__(self):
        return self.user_id

    class Meta:
        verbose_name = "StoreAnswer"
        verbose_name_plural = "StoreAnswers"
        db_table = 'store_answer'


class ParticipantAnswer(AbstractTimeStamp):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    store_id = models.ForeignKey(StoreAnswer, on_delete=models.CASCADE)
    given_ans = models.CharField(max_length=700, null=False, blank=False)
    total_points = models.IntegerField(null=False, blank=False, default='0')
    is_correct = models.BooleanField(null=False, blank=False, default=False)
    def __str__(self):
        return self.question

    class Meta:
        verbose_name = "ParticipantAnswer"
        verbose_name_plural = "ParticipantAnswers"
        db_table = 'participant_answer'

class CategoryWiseLeaderBoard(AbstractTimeStamp):
    user_id = models.CharField(max_length=255, null=True, blank=True)
    category_id = models.CharField(max_length=255, null=True, blank=True)
    cat_point = models.IntegerField(null=True, blank=True, default='0')
    user_name = models.CharField(max_length=255, default='User Name')

    def __str__(self):
        return self.user_name

    class Meta:
        verbose_name = "CategoryWiseLeaderBoard"
        verbose_name_plural = "CategoryWiseLeaderBoards"
        db_table = 'category_wise_leader_board'




