from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from user.models import Users


class Credential(APIView):
    def post(self,request):
        
        email = request.data.get("email")
        password = request.data.get("password")
        if not email or not password:
            return Response({"msg": "Both email and password field are required"},status=status.HTTP_400_BAD_REQUEST)
        try:
            user = Users.objects.get(email=email)
        except Users.DoesNotExist:
            return Response({"msg":"User doesn't exist"},status=status.HTTP_401_UNAUTHORIZED)
        print(request.user)
        print(email)
        if str(request.user) != str(request.data.get("email")):
            return Response({"msg":"Please provide your own detail."},status=status.HTTP_401_UNAUTHORIZED)
        if not user.check_password(password):
            return Response({"msg":"Wrong Password"},status=status.HTTP_401_UNAUTHORIZED)
        return Response({"msg":"Valid User"}, status=status.HTTP_200_OK)
