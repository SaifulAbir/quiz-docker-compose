from django.urls import path
from .views import *

urlpatterns = [
    path('tournament-list/', TournamentListAPIView.as_view()),
    path('tournament-details/<int:id>', TournamentDetailsAPIView.as_view())
]