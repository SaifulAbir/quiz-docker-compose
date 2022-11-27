from requests import Response
from rest_framework.exceptions import ValidationError
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import AllowAny
from django.http import Http404
from question.models import Question, Category, StoreAnswer
from utills.response_wrapper import ResponseWrapper
from question.serializers import QuestionSerializer, CategorySerializer, StoreAnswerSerializer


class CategoriesListAPIView(ListAPIView):
    permission_classes = [AllowAny]
    serializer_class = CategorySerializer
    queryset = Category.objects.all()


class QuestionListAPIView(ListAPIView):
    permission_classes = [AllowAny]
    serializer_class = QuestionSerializer
    queryset = Question.objects.all()
    lookup_field = 'id'
    lookup_url_kwarg = 'id'

    def get_queryset(self):
        cat_id = self.kwargs['id']
        try:
            qtn = Question.objects.filter(category=cat_id)
            return qtn
        except Question.DoesNotExist:
            raise Http404


class StoreAnswerAPIView(CreateAPIView):
    permission_classes = [AllowAny]
    serializer_class = StoreAnswerSerializer
    queryset = StoreAnswer.objects.all()

    def perform_create(self, serializer):
        queryset = Question.objects.filter(id=self.request.data['question_id'])
        if not queryset.exists():
            raise ValidationError('Question Does not Exist')
        else:
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_CREATED)


