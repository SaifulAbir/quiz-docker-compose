from django.urls import path
from .views import *

urlpatterns = [
    path('tournament-list/', TournamentListAPIView.as_view()),
    path('tournament-details/<int:id>', TournamentDetailsAPIView.as_view()),
    path('tournament-question-list/<int:id>/', TournamentQuestionListAPIView.as_view()),
    path('tournament-store-answer/', StoreTournamentAnswerAPIView.as_view()),
    path('tournaament-leaderboard-list/<int:tour_id>/', TournamentWiseLeaderBoardListAPIView.as_view()),
]