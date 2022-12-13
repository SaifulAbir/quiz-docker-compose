from rest_framework import serializers
from .models import Category, Question, QuestionChoice, StoreAnswer, CategoryWiseLeaderBoard


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = (
            'id',
            'title',
        )


class QuestionChoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuestionChoice
        fields = (
            'id',
            'title',
            'is_answer'
        )


class QuestionSerializer(serializers.ModelSerializer):
    question_choice = QuestionChoiceSerializer(many=True)

    class Meta:
        model = Question
        fields = (
            'id',
            'category',
            'title',
            'level',
            'question_choice',
        )


class StoreAnswerSerializer(serializers.ModelSerializer):

    class Meta:
        model = StoreAnswer
        fields = (
            'user_id',
            'point',
            'cat_id',
            'point',
            # 'question_id',
            # 'answer',
        )

class CategoryWiseLeaderBoardSerializer(serializers.ModelSerializer):

    class Meta:
        model = CategoryWiseLeaderBoard
        fields = (
            'cat_point',
            'user_id',
            'user_name',
        )
