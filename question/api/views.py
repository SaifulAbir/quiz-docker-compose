from rest_framework.generics import ListAPIView
from rest_framework.permissions import AllowAny
from django.http import Http404
from question.models import Question, Category
from question.serializers import QuestionSerializer, CategorySerializer


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


