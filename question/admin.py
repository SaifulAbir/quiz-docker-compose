from django.contrib import admin
from question.models import Question, QuestionChoice, Category

admin.site.register(Question)
admin.site.register(QuestionChoice)
admin.site.register(Category)
