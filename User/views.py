from django.shortcuts import render
from django.conf import settings
#from django.http.response import HttpResponse, JsonResponse
from rest_framework.response import Response
from rest_framework.views import APIView
from User.models import *
from django.views.decorators.csrf import csrf_exempt
# from django.views.decorators.csrf import csrf_exempt
# Create your views here.
from django.db.models import Q
from rest_framework import viewsets, status
import jwt
from django.conf import settings
import random
from django.http import JsonResponse

class SignupAPIView(APIView):
    @csrf_exempt
    def post(self,request):
        data = request.data

        user_name=data.get('user_name')
        mail=data.get('mail')
        password=data.get('password')

        if CustomUser.objects.filter(Q(user_name=user_name)).exists():
            return Response({'Error':'User Already Exists'})
        else:
            data=CustomUser.objects.create(user_name=user_name)
            auth_token=jwt.encode(
                                    {
                                        'user_name':user_name,
                                    },
                                    str(settings.JWT_SECRET_KEY), algorithm="HS256")
                                    #print(auth_token,'this is auth_token')

            authorization = 'Bearer'+' '+str(auth_token)
            print(auth_token,'this is auth_token')
            response_result = {}
            response = {}
            response_result['result'] = {
                            'result': {'Data': 'User Successfully Registered',
                            'token':authorization,
                            'user_id':data.id,
                            "user_name":user_name,

                            }}
            response['Authorization'] = authorization
            response['status'] = status.HTTP_200_OK
            return Response(response_result['result'], headers=response,status= status.HTTP_200_OK)



class LoginAPIView(APIView):
    #breakpoint()
    def post(self,request):
        data = request.data
        user_name =data.get("user_name")
        response = {}
        if CustomUser.objects.filter(Q(user_name=user_name)).exists():
            user =CustomUser.objects.get(Q(user_name=user_name))
            #data_dict = {}
            if user:
                auth_token = jwt.encode(
                    {'user_id':user.id,'user_name':user_name},
                    str(settings.JWT_SECRET_KEY), algorithm="HS256")
                authorization = 'Bearer'+' '+str(auth_token)
                response_result = {}
                response = {}
                response_result['result'] = {
                    'detail': 'Login successfull',
                    'user_id':user.id,
                    'token':authorization,
                    'status': status.HTTP_200_OK
                    }
                response['Authorization'] = authorization
                response['status'] = status.HTTP_200_OK
                return Response(response_result['result'], headers=response,status= status.HTTP_200_OK)
            else:
                header_response = {}
                response['error'] = {'error': {
                    'detail': 'Invalid Username / Password', 'status': status.HTTP_401_UNAUTHORIZED}}
                return Response(response['error'], headers=header_response,status= status.HTTP_401_UNAUTHORIZED)
        else:

            response['error'] = {'error': {
                    'detail': 'Invalid Username / Password', 'status': status.HTTP_401_UNAUTHORIZED}}
            return Response(response['error'], status= status.HTTP_401_UNAUTHORIZED)





from django.contrib.auth import authenticate
from django.core.mail import message, send_mail, EmailMessage
import inspect

otpsss= random.randint(100000, 999999)
forgotpass_otps=otpsss
class ForgotPassword_send_otp(APIView):

    def post(self, request):
        data = request.data

        user_name = data.get('user_name')

        user_check=CustomUser.objects.filter(user_name=user_name)
        for i in user_check:
            mail=i.mail
        if user_check:
            message = inspect.cleandoc('''Hello,\n%s is your OTP to Forgot Password to your jobportal.\nWith Warm Regards,\njobportal,
                                   ''' % (otpsss))
            send_mail(
                'Greetings from Amx fibergrid', message
                ,
                'poojakumariip3@gmail.com',
                [mail],

            )
            data_dict = {}
            data_dict["Otp"] = otpsss
            return JsonResponse(data_dict, safe=False)

        else:
            response="Invalid username"
            return Response(response, status=status.HTTP_400_BAD_REQUEST)

class OTP_Verification_forgotpassAPIView(APIView):


    def post(self, request):
        data = request.data
        otp = data.get('otp')
        print(forgotpass_otps,'ori')
        print(otp,'ori')
        if otp:
            if int(otp)==int(forgotpass_otps):
                response="OTP matcheds successfully"
                return Response(response, status=status.HTTP_200_OK)
            else:
                response="Invalid otp"
                return Response(response, status=status.HTTP_400_BAD_REQUEST)
        else:
            response="otp required"
            return Response(response, status=status.HTTP_400_BAD_REQUEST)

#
# class ForgotPasswordUpdate(APIView):
#
#     def post(self, request):
#         data = request.data
#         username = data.get('user_name')
#         password = data.get('new_password')
#         confirm_password = data.get('confirm_password')
#
#         user_check = CustomUser.objects.filter(user_name= user_name)
#
#         if password == confirm_password:
#             if user_check:
#                 user_data = User.objects.get(user_name= user_name)
#                 user_data.set_password(password)
#                 user_data.save()
#
#                 message= 'Hello!\nYour password has been updated sucessfully. '
#                 subject= 'Password Updated Sucessfully '
#
#                 email = EmailMessage(subject, message, to=[user_data.mail])
#                 email.send()
#                 response="Password Updated Sucessfully"
#                 return Response(response, status=status.HTTP_200_OK)
#
#             else:
#                 response="Please Enter Valid username"
#                 return Response(response, status=status.HTTP_400_BAD_REQUEST)
#         else:
#             response="Password did not matched"
#             return Response(response, status=status.HTTP_400_BAD_REQUEST)




class ForgotPasswordReset(APIView):

    def post(self, request):
        data = request.data

        user_name = data.get('user_name')
        password = data.get('password')
        user_check = User.objects.filter(user_name= user_name)
        if user_check:
            user_data = User.objects.get(user_name= user_name)
            user_data.set_password(password)
            user_data.save()
            message= 'Hello!\nYour password has been updated sucessfully. '
            subject= 'Password Updated Sucessfully '
            email = EmailMessage(subject, message, to=[user_data.mail])
            email.send()
            return Response({'result':{'message': 'Password Updated Sucessfully'}})
        else:
            return Response({'error':{'message': 'Please Enter Valid username'}})
