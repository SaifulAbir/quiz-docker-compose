from rest_framework import serializers
from question.serializers import QuestionSerializer, QuestionChoiceSerializer, CategorySerializer
from .models import Tournament


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
