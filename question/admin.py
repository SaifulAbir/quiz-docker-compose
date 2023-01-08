from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from question.models import Question, QuestionChoice, Category, CategoryWiseLeaderBoard, StoreAnswer


admin.site.register(Category)
admin.site.register(CategoryWiseLeaderBoard)
admin.site.register(StoreAnswer)
# admin.site.register(QuestionChoice)

class QuestionChoiceInline(admin.TabularInline):
    model = QuestionChoice
    fields = ['title', 'is_answer']


@admin.register(Question)
class QuestionAdmin(ImportExportModelAdmin):
    inlines = [
        QuestionChoiceInline
    ]

@admin.register(QuestionChoice)
class QuestionChoiceAdmin(ImportExportModelAdmin):
    pass
