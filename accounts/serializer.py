from urllib import request

from rest_framework import serializers
from django.contrib.auth import get_user_model, authenticate
from django.contrib.auth.password_validation import validate_password
from rest_framework.exceptions import AuthenticationFailed


User = get_user_model()

class SignUpSerializer(serializers.Serializer):
    password=serializers.CharField(write_only=True,min_length=8,validators=[validate_password])
    password2=serializers.CharField(write_only=True)
    class meta:
        model=User
        fields=('username','email','password','phone')

    def validate_password(self,attrs):
        if attrs['password'] != attrs.pop['password2']:
            raise serializers.ValidationError('Passwords must match')
        return attrs
    def create(self,validated_data):
        user=User.objects.create(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password'],
            phone=validated_data['phone'],

        )

class loginSerializer(serializers.Serializer):
    email=serializers.EmailField()
    password=serializers.CharField(write_only=True)
    def validate(self,attrs):
        email=attrs.get['email',''].lower()
        password=attrs.get['password']
        user=authenticate(request=self.context.get[request],username=email,password=password)
        if not user:
            raise AuthenticationFailed("Invalid username and/or password.")
        if not user.is_active:
            raise AuthenticationFailed("Account disabled.")
        attrs['user']=user
        return attrs
