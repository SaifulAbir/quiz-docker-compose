from django.urls import path
from .views import *

urlpatterns = [
    path('category-list/', CategoriesListAPIView.as_view()),
    path('question-list/<int:id>/', QuestionListAPIView.as_view()),
    path('store-answer/', StoreAnswerAPIView.as_view()),
    path('category-leaderboard-list/<int:cat_id>/', CategoryLeaderboardListAPIView.as_view()),
]