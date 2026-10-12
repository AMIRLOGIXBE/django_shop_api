# from multiprocessing import context
#
# from django.contrib.auth import authenticate
# from django.template.context_processors import request
# from rest_framework import serializers
# from rest_framework.response import Response
# from rest_framework.views import APIView
# from rest_framework_simplejwt.tokens import RefreshToken
#
# from accounts.forms import get_user_model
# from accounts.serializer import SignUpSerializer, loginSerializer
#
# user= get_user_model()
# from products import serializer
#
#
# class sign_up_view(APIView):
#     def post(self,request):
#         serializer=SignUpSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         user = serializer.save()
#         refresh = RefreshToken.for_user(user)
#         return Response({status,message,refresh,acces}status)
# class login_view(APIView):
#     def post(self,request):
#         serializer=loginSerializer(data=request.data,context={'request':request})
#         serializer.is_valid(raise_exception=True)
#         user = serializer.validated_data['user']
#         refresh = RefreshToken.for_user(user)
#         re
#
#
# # class signup(serializers.Serializer):
# #     password=serializers.CharField(write_only=True,min_length=8)
# #     password2=serializers.CharField(write_only=True)
# #     class meta:
# #         model=user
# #         fields=('username','email','password','phone')
# #         def validate_password(self,attrs):
# #             if attrs["password"] != attrs["password2"]:
# #                 raise serializers.ValidationError("Passwords don't match")
# #             return attrs
# #         def create(self,validated_data):
# #             user=User.objects.create_user(validated_data["username"],validated_data["email"],validated_data["password"])
# # class login(serializers.Serializer):
# #     email=serializers.EmailField()
# #     password=serializers.CharField(write_only=True)
# #     def validate(self,attrs):
# #         email=attrs.get("email",'').lower()
# #         password=attrs.get("password")
# #         user=authenticate(request=self.context.get[request],username=email,password=password)
# #         if not user:
# #             raise serializers.ValidationError("Invalid credentials")
# #         attrs['user']=user
# #         return attrs
#
#
