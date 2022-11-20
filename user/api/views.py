from time import time
import pytz
from django.conf import settings
from django.contrib.auth.hashers import check_password, make_password
from django.db.models import Q
from datetime import datetime
from rest_framework import viewsets, mixins, status, generics
from rest_framework.decorators import api_view
from rest_framework.exceptions import ValidationError
from rest_framework.generics import RetrieveUpdateAPIView, CreateAPIView, ListAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate
from rest_framework.status import HTTP_401_UNAUTHORIZED, HTTP_200_OK
from rest_framework.utils import json
from rest_framework_simplejwt.tokens import RefreshToken

from configs.SMSConfig import OTPManager
# from ecommerce.common.emails import send_email_without_delay
from external.validation.data_validator import check_dict_data_rise_error
from user import models as user_models
import jwt
from django.template.loader import render_to_string
from user import serializers as user_serializers
from user.models import *
from rest_framework.views import APIView
from user.serializers import  *
from django.core.validators import RegexValidator
import re
from utills.response_wrapper import ResponseWrapper


# class RegisterUser(mixins.CreateModelMixin,
#                    mixins.RetrieveModelMixin,
#                    viewsets.GenericViewSet):
#     queryset = user_models.User.objects.all()
#     serializer_class = user_serializers.UserRegisterSerializer
#     permission_classes = [AllowAny]
#
#     def create(self, request):
#         serializer = user_serializers.UserRegisterSerializer(data=request.data)
#
#         if serializer.is_valid():
#             serializer.save()
#             user = user_models.User.objects.none()
#             try:
#                 user = user_models.User.objects.get(
#                     email=request.data["email"])
#
#                 token = RefreshToken.for_user(user)
#
#                 exp = time() + 1200 #20 minutes
#                 email_list = request.data["email"]
#                 subject = "Verify Your Account"
#                 token = jwt.encode({'email': email_list, 'exp': exp, 'scope': subject},
#                                    settings.JWT_SECRET, algorithm='HS256')
#                 html_message = render_to_string('verification_email.html', {'token': token, 'domain': settings.EMAIL_DOMAIN_NAME})
#                 send_email_without_delay(subject, html_message, email_list)
#                 CustomerProfile.objects.create(user=user)
#                 data = {
#                     "user_id": user.id,
#                     "email": user.email,
#                     "full_name": user.first_name + " " + user.last_name
#                 }
#                 return Response({"status": True, "data": data}, status=status.HTTP_200_OK)
#             except (user_models.User.DoesNotExist):
#                 if user:
#                     user.delete()
#                 return Response({"status": False, "data": {"message": "User not registered. Please try again."}}, status=status.HTTP_409_CONFLICT)
#         else:
#             return Response({"status": False, "data": {"message": "User not registered. Please try again.", "errors": serializer.errors}}, status=status.HTTP_406_NOT_ACCEPTABLE)


# class SetPasswordAPIView(CreateAPIView):
#     queryset = User.objects.all()
#     serializer_class = SetPasswordSerializer
#     permission_classes = [AllowAny]

#     def post(self, request, *args, **kwargs):
#         email = check_dict_data_rise_error("email", request_data=request.data, arrise=True)
#         phone = check_dict_data_rise_error("phone", request_data=request.data, arrise=True)
#         password = check_dict_data_rise_error("password", request_data=request.data, arrise=True)
#         try:
#             user = User.objects.get(phone=phone, email=email)
#         except User.DoesNotExist:
#             user = None
#         if user:
#             user.set_password(password)
#             user.is_active = True
#             user.save()
#             return Response(
#                 data={"user_id": user.id if user else None, "details": "Password setup successful"},
#                 status=status.HTTP_201_CREATED)
#         else:
#             return Response(
#                 data={"user_id": user.id if user else None, "details": "Password setup not successful"},
#                 status=status.HTTP_400_BAD_REQUEST)


class SendOTPAPIView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = OTPSendSerializer
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        if request.data.get("phone"):
            phone = request.data.get("phone")
            try:
                otp = OTPModel.objects.get(contact_number=phone)
                otp_sending_time = datetime.now(pytz.timezone('Asia/Dhaka'))
                otp.otp_number = OTPManager().initialize_otp_and_sms_otp(phone)
                otp.expired_time = otp_sending_time
                otp.save()
        
            except OTPModel.DoesNotExist:
                otp_sending_time = datetime.now(pytz.timezone('Asia/Dhaka'))
                otp = OTPModel.objects.create(contact_number=phone, otp_number=OTPManager().initialize_otp_and_sms_otp(phone), expired_time=otp_sending_time)

            return ResponseWrapper(data={"contact_number": otp.contact_number,"otp_number": otp.otp_number}, status=200)  
                
        else:
            return ResponseWrapper(
                error_msg="Phone number is required", status=400
            )


class ReSendOTPAPIView(CreateAPIView):
    queryset = OTPModel.objects.all()
    serializer_class = OTPReSendSerializer
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        contact_number = request.data.get("contact_number")
        if contact_number:
            sent_otp = OTPManager().initialize_otp_and_sms_otp(contact_number)
            otp_sending_time = datetime.now(pytz.timezone('Asia/Dhaka'))
            try:
                otp_obj = OTPModel.objects.get(contact_number=contact_number)
                otp_obj.otp_number = sent_otp
                otp_obj.expired_time = otp_sending_time
                otp_obj.save()
            except OTPModel.DoesNotExist:
                otp_obj = None
            if not otp_obj:
                return ResponseWrapper(
                    error_msg="Number doesn't exists", status=400
                )
            # return Response(
            #     data={"sent_otp": sent_otp},
            #     status=status.HTTP_201_CREATED)
            return ResponseWrapper(data={"sent_otp": sent_otp}, status=200)
        else:
            return ResponseWrapper(
                error_msg="Phone number is required", status=400
            )



class OTPVerifyAPIVIEW(CreateAPIView):
    """
       Get OTP from user, and verify it
    """
    serializer_class = OTPVerifySerializer
    queryset = OTPModel.objects.all()
    permission_classes = [AllowAny, ]

    def post(self, request, *args, **kwargs):
        contact_number = request.data.get("contact_number")
        otp_number = request.data.get("otp_number")
        try:
            otp_obj = OTPModel.objects.filter(contact_number=contact_number).last()
            if str(otp_obj.otp_number) == otp_number:
                otp_obj.verified_phone = True
                otp_sent_time = otp_obj.expired_time
                timediff = datetime.now(pytz.timezone('Asia/Dhaka')) - otp_sent_time
                time_in_seconds = timediff.total_seconds()

                if time_in_seconds > 120:
                    return ResponseWrapper(error_msg="time expired", status=408)
                try:
                    user = User.objects.get(phone=contact_number)
                    token = RefreshToken.for_user(user) 
                except:
                    user = None
                    user = User.objects.create(
                    phone=contact_number,
                    is_active=True
                    )
                    user.save()
                    token = RefreshToken.for_user(user)

                otp_obj.save()
                return ResponseWrapper(
                        data={
                            "refresh": str(token) if token else None,
                            "access": str(token.access_token) if token else None,
                            "user_id": user.id,
                            "phone": user.phone,
                            "is_active": user.is_active
                        },
                        status=200
                    )
            else:
                return ResponseWrapper(error_msg="Incorrect OTP", status=400)
    
        except Exception as e:
            return ResponseWrapper(error_msg="Number doesn't exists", status=406)


# class LoginUser(mixins.CreateModelMixin,
#                 viewsets.GenericViewSet):
#     serializer_class = user_serializers.LoginSerializer
#     permission_classes = [AllowAny]

#     @csrf_exempt
#     def create(self, request):
#         serializer = user_serializers.LoginSerializer(data=request.data)
#         if serializer.is_valid():
#             email = request.data["email"]
#             password = request.data["password"]
#             try:
#                 check = user_models.User.objects.get(email=email)
#                 user = authenticate(
#                     request, username=request.data["email"], password=request.data["password"])
#             except (user_models.User.DoesNotExist, Exception):
#                 return Response({"status": False, "data": {"message": "Invalid credentials"}}, status=status.HTTP_404_NOT_FOUND)
#             if user:
#                 token = RefreshToken.for_user(user)
#                 data = {
#                     "user_id": user.id,
#                     "email": user.email,
#                     "name": user.name,
#                     "access_token": str(token.access_token),
#                     "refresh_token": str(token)
#                 }
#                 return Response({"status": True, "data": data}, status=status.HTTP_200_OK)
#             else:
#                 return Response({"status": False, "data": {"message": "Invalid credentials"}}, status=status.HTTP_406_NOT_ACCEPTABLE)
#         else:
#             return Response({"status": False, "data": {"message": "Invalid credentials", "error": serializer.errors}}, status=status.HTTP_406_NOT_ACCEPTABLE)


# class VerifyUserAPIView(APIView):
#     permission_classes = [AllowAny]
#     lookup_url_kwarg = "verification_token"

#     def get(self,  *args, **kwargs):
#         verification_token = kwargs.get(self.lookup_url_kwarg)
#         try:
#             payload = jwt.decode(jwt=verification_token, key=settings.JWT_SECRET, algorithms=['HS256'])
#             user = User.objects.get(email=payload['email'])
#             if not user.is_active:
#                 user.is_active = True
#                 user.save()
#             return Response({"message": "Successfully activated"}, status=status.HTTP_200_OK)
#         except jwt.ExpiredSignatureError:
#             return Response({"message": "Token expired. Get new one"}, status=status.HTTP_401_UNAUTHORIZED)


# class CustomerRetrieveUpdateAPIView(RetrieveUpdateAPIView):
#     serializer_class = CustomerProfileUpdateSerializer
#
#     def get_object(self):
#         customer = CustomerProfile.objects.get(user=self.request.user)
#         return customer
#
#     # def put(self, request, *args, **kwargs):
#     #     return self.update(request, *args, **kwargs)


# class SubscriptionAPIView(CreateAPIView):
#     permission_classes = [AllowAny]
#     serializer_class = SubscriptionSerializer

#     def post(self, request, *args, **kwargs):
#         return super(SubscriptionAPIView, self).post(request, *args, **kwargs)


# @api_view(["POST"])
# def change_password(request):
#     received_json_data = json.loads(request.body)
#     user = request.user.id
#     try:
#         old_password = received_json_data["old_password"]
#     except KeyError:
#         raise ValidationError("Old password cannot be blank.")
#     try:
#         new_password = received_json_data["new_password"]
#     except KeyError:
#         raise ValidationError("New password cannot be blank.")
#
#     try:
#         user_obj = User.objects.get(id=user)
#     except User.DoesNotExist:
#         data = {
#             'status': 'failed',
#             'code': HTTP_401_UNAUTHORIZED,
#             "message": "User is not exists",
#             "result": ''
#         }
#         return Response(data, HTTP_401_UNAUTHORIZED)
#     status = check_password(old_password, user_obj.password)
#
#     if not status :
#         data = {
#             'status': 'failed',
#             'code': HTTP_401_UNAUTHORIZED,
#             "message": "Your old password is wrong",
#             "result": ''
#         }
#         return Response(data, HTTP_401_UNAUTHORIZED)
#     else:
#         new_password = make_password(new_password)
#         user_obj.password = new_password
#         user_obj.save()
#
#         data = {
#             'status': 'success',
#             'code': HTTP_200_OK,
#             "message": "Password changed successfully",
#             "result": {
#                 "user": {
#                     "username": user_obj.username,
#                     'user_id': user_obj.id
#                 }
#             }
#         }
#     return Response(data, HTTP_200_OK)


# class UserListAPIView(ListAPIView):
#     queryset = User.objects.filter()
#     permission_classes = [AllowAny]
#     serializer_class = UserRegisterSerializer


# class ChangePasswordView(generics.UpdateAPIView):
#     permission_classes = (IsAuthenticated,)
#     serializer_class = ChangePasswordSerializer

#     def get_object(self):
#         return self.request.user