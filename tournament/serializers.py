from rest_framework import serializers
# from question.serializers import QuestionSerializer, QuestionChoiceSerializer, CategorySerializer
from .models import Tournament, TournamentQuestion, TournamentQuestionChoice


class TournamentListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tournament
        fields = (
            'id',
            'title',
            'description',
            'published',
            'banner',
   )


class TournamentDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tournament
        fields = '__all__'


class TournamentQuestionChoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = TournamentQuestionChoice
        fields = (
            'id', 'title', 'is_answer'
        )


class TournamentQuestionSerializer(serializers.ModelSerializer):
    choice = TournamentQuestionChoiceSerializer(many=True)

    class Meta:
        model = TournamentQuestion
        fields = (
            'id', 'tournament', 'title', 'choice'
        )
