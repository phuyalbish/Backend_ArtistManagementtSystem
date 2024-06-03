from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from user.serializers import UserSerializer
from user.models import Users
from rest_framework.permissions import AllowAny
from rest_framework.exceptions import PermissionDenied


class CreateUser(APIView):
    permission_classes = [AllowAny]
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if not request.user.is_superuser and serializer.data["is_staff"]:
            raise PermissionDenied("You do not have permission to perform this action.")
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=422)