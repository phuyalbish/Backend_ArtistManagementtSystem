from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from user.models import Users
from user.serializers import UserSerializer

class Login(APIView):
    def post(self,request):
        email = request.data.get("email")
        password = request.data.get("password")

        if not email or not password:
            return Response({"msg": "Both email and password field are required"},status=status.HTTP_400_BAD_REQUEST)
        
        user = Users.objects.get(email=email)
        if user == None:
            return Response({"msg":"User doesn't exist"},status=status.HTTP_401_UNAUTHORIZED)
        
        if not user.check_password(password):
            return Response({"msg":"Wrong Password"},status=status.HTTP_401_UNAUTHORIZED)
        
        serializer = UserSerializer(user)
        token = RefreshToken.for_user(user)

        return Response({
            'refresh_token':str(token),
            'access_token':str(token.access_token),
            'user': serializer.data
        })