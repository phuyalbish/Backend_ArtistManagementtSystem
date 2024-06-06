from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from user.serializers import UserSerializer
from user.models import Users
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import PermissionDenied



class EditUser(APIView):
    permission_classes = [IsAuthenticated]
    def patch(self, request,userid):
        try:
            user = Users.objects.get(id=userid)
        except Users.DoesNotExist:
            return Response({"msg": "User not found"}, status=status.HTTP_404_NOT_FOUND)
        if user != request.user and not request.user.is_staff and not request.user.is_superuser:
            raise PermissionDenied("You do not have permission to perform this action.")
        if  request.user.is_staff and user.is_superuser:
            raise PermissionDenied("You do not have permission to perform this action.")
        serializer = UserSerializer(instance=user, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)