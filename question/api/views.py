from requests import Response
from rest_framework.exceptions import ValidationError
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import AllowAny
from django.http import Http404
from question.models import Question, Category, StoreAnswer, CategoryWiseLeaderBoard
from user.models import User
from utills.response_wrapper import ResponseWrapper
from question.serializers import QuestionSerializer, CategorySerializer, StoreAnswerSerializer, CategoryWiseLeaderBoardSerializer
from random import randint


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
        i = randint(0, Question.objects.count() - 1)
        cat_id = self.kwargs['id']
        try:
            qtn = Question.objects.filter(category=cat_id).order_by('?')[:10]
            return qtn
        except Question.DoesNotExist:
            raise Http404


class StoreAnswerAPIView(CreateAPIView):
    permission_classes = [AllowAny]
    serializer_class = StoreAnswerSerializer

    def post(self, request, *args, **kwargs):
        user_id = request.data['user_id']
        point_rec = request.data['point']
        cat = request.data['cat_id']
        user = User.objects.get(id=user_id)
        point = user.point

        point += point_rec
        user.point=point
        user.save()
        try:
            catstore = CategoryWiseLeaderBoard.objects.filter(category_id=cat)
            catuserdata = catstore.get(user_id=user_id)
            catuserdata.cat_point += point_rec
            catuserdata.save()
            print(catuserdata)
        except:
            CategoryWiseLeaderBoard.objects.create(
                user_id=user_id,
                category_id =cat,
                cat_point =point_rec,
                user_name = user.full_name,
            )

        return super(StoreAnswerAPIView, self).post(request,*args,**kwargs)

class CategoryLeaderboardListAPIView(ListAPIView):
    permission_classes = [AllowAny]
    serializer_class = CategoryWiseLeaderBoardSerializer
    lookup_field = 'cat_id'
    lookup_url_kwarg = "cat_id"

    def get_queryset(self):
        cat_id = self.kwargs['cat_id']
        print(cat_id)
        if cat_id:
            try:
                leader = CategoryWiseLeaderBoard.objects.filter(category_id=cat_id).order_by("-cat_point")
                return leader

                # name = []
                # point = []
                # for lead in leader:
                #     single_user = User.objects.get(id=lead.user_id)
                #     if single_user.full_name:
                #         name.append(single_user.full_name)
                #     else:
                #         name.append("user name")
                #     point.append(lead.cat_point)
                # print(name,point)


            except:
                pass


        #         queryset = Product.objects.filter(
        #             vendor=vendor, status='ACTIVE').order_by('-created_at')
        #     except:
        #         raise ValidationError({"details": "Vendor Not Valid.!"})
        # else:
        #     queryset = Product.objects.filter(
        #         status='ACTIVE').order_by('-created_at')
        # return queryset
