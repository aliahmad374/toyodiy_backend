from rest_framework import serializers
from xml.dom import ValidationErr
from account.models import User
from django.utils.encoding import smart_str,force_bytes,DjangoUnicodeDecodeError
from django.utils.http import urlsafe_base64_decode,urlsafe_base64_encode
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from account.utils import Util
from django.contrib.auth.models import Group
from django.db import models
import random
import string


def generate_password(length=10):
    characters = string.ascii_letters + string.digits
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

class UserRegistrationSerializer(serializers.ModelSerializer):
    groups = serializers.SlugRelatedField(many=True, slug_field='name', queryset=Group.objects.all())
    class Meta:
        model = User
        fields = ['email','first_name','last_name','address','phone','tc','is_verified','password','groups']
        extra_kwargs = {
            'password':{'write_only':True}
        }

    def create(self, validated_data):
        groups_data = validated_data.pop('groups', [])  # Extract the groups data from validated_data
        user = User.objects.create_user(**validated_data)
        # Add the user to the specified groups
        for group_name in groups_data:
            try:
                group = Group.objects.get(name=group_name)
                user.groups.add(group)
            except Group.DoesNotExist:
                raise serializers.ValidationError(f"Group '{group_name}' does not exist.")
        
        return user
    
class ReUserVerificationSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(max_length=255)
    class Meta:
        model = User        
        fields = ['email']    
    

class UserLoginSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(max_length=255)
    class Meta:
        model = User
        fields = ['email','password']


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model= User
        fields = ['id','email','first_name','last_name']

class UserChangePasswordSerializer(serializers.Serializer):
    password = serializers.CharField(max_length=255,style={'input_type':'password'},write_only=True)
    
    class Meta:
        fields = ['password']

    def validate(self, attrs):
        password  =attrs.get('password')
        user = self.context.get('user')
        if password=="":
            raise serializers.ValidationError("Password cannot be empty")
        user.set_password(password) 
        user.save()
        return attrs  
    

class SendPasswordResetEmailSerializer(serializers.Serializer):
    email = serializers.EmailField(max_length=255)
    class Meta:
        fields = ['email']

    def validate(self, attrs):
        email = attrs.get('email')
        if User.objects.filter(email=email).exists():
            if User.objects.get(email=email).is_verified==True:
                user = User.objects.get(email=email)
                new_password = generate_password()
                user.set_password(str(new_password)) 
                user.save()
                # uid= urlsafe_base64_encode(force_bytes(user.id))
                # token = PasswordResetTokenGenerator().make_token(user)
                # link = 'http://127.0.0.1:8000/user/reset-password/'+uid+'/'+token+'/'
                # body = 'http://127.0.0.1:8000/user/reset-password/'+uid+'/'+token+'/'
                # body = 'Click Following Link to reset Your Password'+link
                data = {
                    'subject':"Reset Your Password",
                    'body':new_password,
                    'to_email':user.email
                }
                try:
                    Util.send_email(data,user.first_name,True)
                except:
                    raise serializers.ValidationError('error in your smtp authentication')

                return attrs
            else:
                raise serializers.ValidationError('You are not verified user Please Verify Your Email')

        else:
            raise serializers.ValidationError('You are not a Registered user')
        

class UserpasswordResetSerializer(serializers.Serializer):
    password = serializers.CharField(max_length=255,style={'inpuy_type':'password'},write_only=True)  
    class Meta:
        fields = ['password']

    def validate(self, attrs):
        try:
            password  =attrs.get('password')
            # password2  =attrs.get('password2')
            uid = self.context.get('uid')
            token = self.context.get('token')
            if password=="":
                raise serializers.ValidationError("Password cannot be empty")
            id = smart_str(urlsafe_base64_decode(uid))
            user = User.objects.get(id=id)
            if not PasswordResetTokenGenerator().check_token(user,token):
                raise serializers.ValidationError("Token is Not Valid or Expired")        

            user.set_password(password) 
            user.save()
            return attrs
        except DjangoUnicodeDecodeError as identifier:
            PasswordResetTokenGenerator().check_token(user,token)
            raise serializers.ValidationError("Token is Not Valid or Expired")
    
        
         
