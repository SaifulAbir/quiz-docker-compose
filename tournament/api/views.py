from rest_framework.exceptions import ValidationError
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import AllowAny
from tournament.serializers import TournamentListSerializer, TournamentDetailsSerializer,\
    TournamentQuestionChoiceSerializer, TournamentQuestionSerializer, StoreTournamentAnswerSerializer, \
    TournamentWiseLeaderBoardSerializer
from tournament.models import Tournament, TournamentQuestion, TournamentWiseLeaderBoard
from user.models import User
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
            raise ValidationError({"msg": "No tournament available! "})


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


class StoreTournamentAnswerAPIView(CreateAPIView):
    permission_classes = [AllowAny]
    serializer_class = StoreTournamentAnswerSerializer

    def post(self, request, *args, **kwargs):
        user_id = request.data['user_id']
        point_rec = request.data['point']
        tournament = request.data['tournament_id']
        user = User.objects.get(id=user_id)
        point = 0

        point += point_rec
        try:
            tour_store = TournamentWiseLeaderBoard.objects.filter(tournament_id=tournament)
            tour_user_data = tour_store.get(user_id=user_id)
            tour_user_data.tour_point += point_rec
            tour_user_data.save()
        except:
            TournamentWiseLeaderBoard.objects.create(
                user_id=user_id,
                tournament_id=tournament,
                tour_point=point_rec,
                user_name=user.full_name,
            )
        return super(StoreTournamentAnswerAPIView, self).post(request, *args, **kwargs)


class TournamentWiseLeaderBoardListAPIView(ListAPIView):
    permission_classes = [AllowAny]
    serializer_class = TournamentWiseLeaderBoardSerializer
    lookup_field = 'tour_id'
    lookup_url_kwarg = "tour_id"

    def get_queryset(self):
        tour_id = self.kwargs['tour_id']
        # print(tour_id)
        if tour_id:
            try:
                leader_board = TournamentWiseLeaderBoard.objects.filter(tournament_id=tour_id).order_by("-tour_point")
                return leader_board
            except:
                pass