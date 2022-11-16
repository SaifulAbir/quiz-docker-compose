from django.urls import path
from django.views.decorators.csrf import csrf_exempt
from user.api.views import LoginUser, VerifyUserAPIView,  \
    SubscriptionAPIView,  ChangePasswordView, SendOTPAPIView, OTPVerifyAPIVIEW, ReSendOTPAPIView, \
    SetPasswordAPIView

urlpatterns = [
    path('login/', LoginUser.as_view({'post': 'create'}), name='login_user'),
    # path('register-user/', csrf_exempt(RegisterUser.as_view({'post': 'create'})), name='register_user'),
    path('send-otp/', SendOTPAPIView.as_view(), name='send_otp'),
    path('otp-verify/', OTPVerifyAPIVIEW.as_view(), name='verify_otp'),
    path('resend-otp/', ReSendOTPAPIView.as_view(), name='resend_otp'),
    path('set-password/', SetPasswordAPIView.as_view(), name='set_password'),
    path('subscription/', SubscriptionAPIView.as_view()),
    path('change_password/', ChangePasswordView.as_view(), name='auth_change_password'),
]