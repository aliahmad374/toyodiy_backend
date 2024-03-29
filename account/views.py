from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from django.contrib.auth import authenticate
from account.serializers import UserRegistrationSerializer,UserLoginSerializer,UserProfileSerializer,UserChangePasswordSerializer,SendPasswordResetEmailSerializer,UserpasswordResetSerializer,ReUserVerificationSerializer
from account.renderers import UserRenderer
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAuthenticated
import jwt
from account.utils import Util
from .models import User
import datetime
from jwt.exceptions import InvalidTokenError
from django.utils import timezone
# Create your views here.
from rest_framework import serializers
from rest_framework_simplejwt.authentication import JWTAuthentication
from datetime import datetime as dt
import pytz

# Generate Token manually
def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)

    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }

def send_verification_email(email,name=None):
    # Generate JWT token with a limited expiration time (60 minutes)
    expires_at = expires_at = timezone.now() + datetime.timedelta(seconds=3600)
    payload = {
    'email': email,
    'exp': expires_at.timestamp()
    }
    token = jwt.encode(payload, 'django-insecure-!&bo@8q95122$@tp3s)ed=xmmqp3))_!#max$@x8j%bj%e&(0p', algorithm='HS256')
    link = f'http://127.0.0.1:8000/user/verify?token={token}'
    # body = 'Click Following Link to reset Your Password'+link
    body = link

    data = {
        'subject':"Account Verification",
        'body':body,
        'to_email':email

    }
    Util.send_email(data,name,None)

class UserRegistrationView(APIView):
    renderer_classes = [UserRenderer]
    def post(self,request,format=None):
        serializer = UserRegistrationSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            user = serializer.save()           
            try:            
                send_verification_email(user.email,serializer.data['first_name'])
            except Exception as E:
                Response({'msg':'error'+str(E)},status=status.HTTP_400_BAD_REQUEST)

            return Response({'msg':'Registration Successfull'},status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
class ReUserVerificationView(APIView):
    renderer_classes = [UserRenderer]
    def post(self,request,format=None):
        serializer = ReUserVerificationSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            user = User.objects.get(email=serializer.data['email'])
            if user.is_verified==False:
                try:
                    send_verification_email(serializer.data['email'],user.first_name)
                except Exception as E:
                    Response({'msg':'error'+str(E)},status=status.HTTP_400_BAD_REQUEST)

                return Response({'msg':'Email Verification Send'},status=status.HTTP_201_CREATED)
            else:
                return Response({'msg':'You are already a Verified User Please Login again'},status=status.HTTP_201_CREATED)

        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)    
    

class UserVerificationView(APIView):
    def get(self, request):
        token = request.GET.get('token')

        if token:
            try:
                decoded_token = jwt.decode(token, 'django-insecure-!&bo@8q95122$@tp3s)ed=xmmqp3))_!#max$@x8j%bj%e&(0p', algorithms=['HS256'])
                email = decoded_token.get('email')

                # Perform any necessary actions here, such as marking the user as verified
                try:
                    user = User.objects.get(email=email)
                    user.is_verified = True
                    user.save()
                except User.DoesNotExist:
                    return Response({'msg': 'Username Doest not Exist'}, status=status.HTTP_401_UNAUTHORIZED)

                # Redirect the user to the login page or any other relevant page
                return Response({'msg': 'Now you can log in'}, status=status.HTTP_200_OK)
            
            except jwt.ExpiredSignatureError:
                return Response({'error': 'Token has expired.'}, status=status.HTTP_400_BAD_REQUEST)
            
            except InvalidTokenError as e:
                return Response({'error': 'Invalid token: ' + str(e)}, status=status.HTTP_400_BAD_REQUEST)
            
        else:
            return Response({'error': 'Token not provided.'}, status=status.HTTP_400_BAD_REQUEST)
        

class UserLoginView(APIView):
    renderer_classes = [UserRenderer]
    def  post(self,request,format=None):
        serializer = UserLoginSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            email = serializer.data.get('email')
            password = serializer.data.get('password') 
            try:           
                user = authenticate(email=email,password=password)
                created_date = user.created_at
            except:
                return Response({'errors':{'msg':['user is not authenticated']}},status=status.HTTP_404_NOT_FOUND)

            
            
            if user is not None:

                today_date = dt.now(pytz.utc)
                difference = today_date - created_date
                hours = difference.total_seconds() // 3600
                try:
                    # user_verify = User.objects.get(email=email)
                    if user.is_verified==True:
                        token = get_tokens_for_user(user)
                        return Response({'token':token,'msg':'Login Successfully'},status=status.HTTP_200_OK)
                    elif user.is_verified==False and hours<1:
                        return Response({'errors':{'msg':['please check your email to verify']}},status=status.HTTP_200_OK)
                    else:
                        return Response({'errors':{'msg':['Reverify User']}},status=status.HTTP_200_OK)
                except Exception as E:
                    return Response({'errors':{'msg':['Error']}},status=status.HTTP_404_NOT_FOUND)
                    


            else:
                return  Response({'errors':{'non_field_errors':['Email or password is not Valid']}},status=status.HTTP_404_NOT_FOUND)
            

class UserProfileView(APIView):
    renderer_classes =[UserRenderer]
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]
    def get(self,request,format=None):
        serializer = UserProfileSerializer(request.user)
        new_item = serializer.data
        new_item.pop('id', None)
        new_item.pop('email', None)
        return Response(new_item,status=status.HTTP_200_OK)
    

class UserChangePassword(APIView):
    renderer_classes =[UserRenderer]
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]

    def post(self,request,format=None):
        serializer = UserChangePasswordSerializer(data=request.data,context={'user':request.user})        
        if serializer.is_valid(raise_exception=True):
            return Response({'msg':'Password Changed Succesfully'},status=status.HTTP_200_OK)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    

class SendPasswordResetEmailView(APIView):
    renderer_classes =[UserRenderer]
    def post(self,request,format=None):
        serializer = SendPasswordResetEmailSerializer(data=request.data)      
        if serializer.is_valid(raise_exception=True):
            return Response({'msg':'Password Reset Link Send Please Check Your Email'},status=status.HTTP_200_OK)        
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


    
class UserpasswordResetView(APIView):
    renderer_classes =[UserRenderer]
    def post(self,request,uid,token,format=None):
        serializer = UserpasswordResetSerializer(data=request.data,context={'uid':uid,'token':token})
        if serializer.is_valid(raise_exception=True):
            return Response({'msg':'Password Reset Successfully'})
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST) 
            

class isAdminUser(APIView):
    renderer_classes =[UserRenderer]
    def post(self,request,format=None):        
        email = request.data.get('email')
        if email != None:
            user = User.objects.get(email=email)
            if user.is_admin == True:
                return Response({'success':True},status=status.HTTP_200_OK)
            else:
                return Response({'success':False},status=status.HTTP_200_OK)

        return Response({'error':'required parameter is missing'},status=status.HTTP_400_BAD_REQUEST) 
            


    
        