from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from user.models import Users


class Credential(APIView):
    def post(self,request):
        
        password = request.data.get("password")
        if not password:
            return Response("Password field is required",status=status.HTTP_400_BAD_REQUEST)
        try:
            user = Users.objects.get(id=request.user.id)
        except Users.DoesNotExist:
            return Response("User doesn't exist",status=status.HTTP_401_UNAUTHORIZED)
        if not user.check_password(password):
            return Response("Wrong Password",status=status.HTTP_401_UNAUTHORIZED)
        return Response("Valid User", status=status.HTTP_200_OK)
