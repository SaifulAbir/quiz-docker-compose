from django.contrib import admin
from question.models import Question, QuestionChoice, Category, CategoryWiseLeaderBoard, StoreAnswer

# admin.site.register(Question)
# admin.site.register(QuestionChoice)
admin.site.register(Category)
admin.site.register(CategoryWiseLeaderBoard)
admin.site.register(StoreAnswer)

class QuestionChoiceInline(admin.TabularInline):
    model = QuestionChoice
    fields = ['title', 'is_answer']

@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    inlines = [
        QuestionChoiceInline
    ]