from rest_framework.exceptions import ValidationError
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import AllowAny
from tournament.serializers import TournamentListSerializer, TournamentDetailsSerializer,\
    TournamentQuestionChoiceSerializer, TournamentQuestionSerializer
from tournament.models import Tournament, TournamentQuestion
from django.http import Http404
from random import randint


class TournamentListAPIView(ListAPIView):
    permission_classes = [AllowAny]
    serializer_class = TournamentListSerializer
    queryset = Tournament.objects.all()


class TournamentDetailsAPIView(RetrieveAPIView):
    permission_classes = [AllowAny]
    serializer_class = TournamentDetailsSerializer
    lookup_field = 'id'
    lookup_url_kwarg = "id"

    def get_object(self):
        id = self.kwargs['id']
        query = Tournament.objects.get(id=id)
        if query:
            return query
        else:
            raise ValidationError({"msg": "No tournament available! " })


class TournamentQuestionListAPIView(ListAPIView):
    permission_classes = [AllowAny]
    serializer_class = TournamentQuestionSerializer
    queryset = TournamentQuestion.objects.all()
    lookup_field = 'id'
    lookup_url_kwarg = 'id'

    def get_queryset(self):
        i = randint(0, TournamentQuestion.objects.count() - 1)
        tour_id = self.kwargs['id']
        try:
            qtn = TournamentQuestion.objects.filter(tournament=tour_id).order_by('?')[:10]
            return qtn
        except TournamentQuestion.DoesNotExist:
            raise Http404