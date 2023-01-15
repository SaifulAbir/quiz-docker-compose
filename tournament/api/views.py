from rest_framework.exceptions import ValidationError
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import AllowAny
from tournament.serializers import TournamentListSerializer, TournamentDetailsSerializer
from tournament.models import Tournament
from django.http import Http404


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
            raise ValidationError({"msg": "No Order available! " })