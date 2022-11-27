from django.urls import path
from django.views.decorators.csrf import csrf_exempt
from user.api.views import *

urlpatterns = [
    path('send-otp/', SendOTPAPIView.as_view(), name='send_otp'),
    path('otp-verify/', OTPVerifyAPIVIEW.as_view(), name='verify_otp'),
    path('resend-otp/', ReSendOTPAPIView.as_view(), name='resend_otp'),
    path('user-details/', UserDetailsUpdateView.as_view(), name='user_details'),
]