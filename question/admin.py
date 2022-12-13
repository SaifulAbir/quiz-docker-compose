from django.contrib import admin
from question.models import Question, QuestionChoice, Category, CategoryWiseLeaderBoard

admin.site.register(Question)
admin.site.register(QuestionChoice)
admin.site.register(Category)
admin.site.register(CategoryWiseLeaderBoard)