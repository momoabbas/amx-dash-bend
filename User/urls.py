from django.urls import path, include
from rest_framework import routers
from django.conf import settings
from django.conf.urls.static import static
from .views import *






app_name = 'User'


router = routers.DefaultRouter()


urlpatterns = [
    path('', include(router.urls)),
    path('signup/', SignupAPIView.as_view(), name="SIGNUP"),
    path('login/', LoginAPIView.as_view(), name='LOGIN'),
    path('forgot_password_otp/',ForgotPassword_send_otp.as_view()),
    path('otp_Verification_forgot/',OTP_Verification_forgotpassAPIView.as_view()),
    path('ForgotPasswordUpdate/', ForgotPasswordUpdate.as_view()),

    ]
