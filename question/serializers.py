from rest_framework import serializers
from .models import Category, Question, QuestionChoice


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
            'question_choice',
        )
