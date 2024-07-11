from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from user.serializers import UserSerializer
from user.models import Users
from rest_framework.permissions import IsAuthenticated

from core.permissions import  IsSuperuser
from rest_framework.exceptions import PermissionDenied

from django.db.models import Q
from rest_framework import generics



class EditUser(APIView):
    permission_classes = [IsAuthenticated]
    def patch(self, request):
        try:
            user = Users.objects.get(id=request.user.id)
        except Users.DoesNotExist:
            return Response({"msg": "User not found"}, status=status.HTTP_404_NOT_FOUND)
        if user != request.user and not request.user.is_staff and not request.user.is_superuser:
            raise PermissionDenied("You do not have permission to perform this action.")
        if  request.user.is_staff and user.is_superuser:
            raise PermissionDenied("You do not have permission to perform this action.")
        if not request.user.is_superuser and user.is_staff:
            raise PermissionDenied("You do not have permission to perform this action.")
        serializer = UserSerializer(instance=user, data=request.data, partial=True)
        try:
            Users.objects.exclude(id=request.user.id).get(username=request.data['username'])
            return Response("Username already used", status=status.HTTP_400_BAD_REQUEST)
        except:
            try:
                Users.objects.exclude(id=request.user.id).get(email=request.data['email'])
                return Response("Email already used", status=status.HTTP_400_BAD_REQUEST)
            except:
                if serializer.is_valid():
                    serializer.save()
                    return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class EditStaff(APIView):
    permission_classes = [IsSuperuser]
    def patch(self, request, userid):
        try:
            user = Users.objects.get(id=userid)
        except Users.DoesNotExist:
            return Response({"msg": "User not found"}, status=status.HTTP_404_NOT_FOUND)
        serializer = UserSerializer(instance=user, data=request.data, partial=True)
        try:
            data =  Users.objects.exclude(email=request.data['email']).get(username=request.data['username'])
            return Response("Username already used", status=status.HTTP_400_BAD_REQUEST)
        except:
            try:
                Users.objects.exclude(email=request.data['email']).get(email=request.data['email'])
                return Response("Email already used", status=status.HTTP_400_BAD_REQUEST)
            except:
                if serializer.is_valid():
                    serializer.save()
                    return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)