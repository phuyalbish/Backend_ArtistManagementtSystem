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
        try:
            print(request.data['username'])
            Users.objects.get(username=request.data['username'])
            return Response("Username already used", status=status.HTTP_400_BAD_REQUEST)
        except:
            try:
                Users.objects.get(email=request.data['email'])
                return Response("Email already used", status=status.HTTP_400_BAD_REQUEST)
            except:
                serializer = UserSerializer(data=request.data)
                if serializer.is_valid():
                    validated_data = serializer.validated_data
                    if not request.user.is_superuser and validated_data.get("is_staff"):
                        raise PermissionDenied("You do not have permission to perform this action.")
                    serializer.save()
                    return Response(serializer.data)
                else:
                    return Response(serializer.errors, status=422)


