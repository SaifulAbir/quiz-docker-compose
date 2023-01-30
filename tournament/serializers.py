from rest_framework import serializers
# from question.serializers import QuestionSerializer, QuestionChoiceSerializer, CategorySerializer
from .models import Tournament, TournamentQuestion, TournamentQuestionChoice, StoreTournamentAnswer, TournamentWiseLeaderBoard


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
    tournament_question_choice = TournamentQuestionChoiceSerializer(many=True)

    class Meta:
        model = TournamentQuestion
        fields = (
            'id', 'tournament', 'title', 'tournament_question_choice'
        )


class StoreTournamentAnswerSerializer(serializers.ModelSerializer):

    class Meta:
        model = StoreTournamentAnswer
        fields = (
            'user_id',
            'tournament_id',
            'point',
        )


class TournamentWiseLeaderBoardSerializer(serializers.ModelSerializer):
    class Meta:
        model = TournamentWiseLeaderBoard
        fields = (
            'user_id',
            'tournament_id',
            'tour_point',
            'user_name',
        )
