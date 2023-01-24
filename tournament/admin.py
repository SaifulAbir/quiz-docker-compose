from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from tournament.models import *
# Register your models here.
# admin.site.register(Tournament)
# admin.site.register(TournamentQuestion)
# admin.site.register(TournamentQuestionChoice)


class TournamentQuestionInLine(admin.TabularInline):
    model = TournamentQuestion
    fields = ['title', 'tournament']


class TournamentQuestionChoiceInLine(admin.TabularInline):
    model = TournamentQuestionChoice
    fields = ['title', 'is_answer']

@admin.register(Tournament)
class TournamentAdmin(ImportExportModelAdmin):
    inlines = [
        TournamentQuestionInLine
    ]

@admin.register(TournamentQuestion)
class TournamentQuestionAdmin(ImportExportModelAdmin):
    inlines = [
        TournamentQuestionChoiceInLine
    ]

@admin.register(TournamentQuestionChoice)
class TournamentQuestionChoiceAdmin(ImportExportModelAdmin):
    pass