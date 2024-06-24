from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import os
from user.models import Users
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import PermissionDenied

class ProfileImageRemove(APIView):
    permission_classes = [IsAuthenticated]
    def delete(self, request, pk):
        try:
            user = Users.objects.get(pk=pk)
        except Users.DoesNotExist:
            return Response({"msg": "User not found"}, status=status.HTTP_404_NOT_FOUND)
        if user != request.user and not request.user.is_staff and not request.user.is_superuser:
            raise PermissionDenied("You do not have permission to perform this action.")
        if  request.user.is_staff and user.is_superuser:
            raise PermissionDenied("You do not have permission to perform this action.")
        if not request.user.is_superuser and user.is_staff:
            raise PermissionDenied("You do not have permission to perform this action.")
        
        try:
            if user.img_profile and user.img_profile != 'uploads/default/defaultUser.jpg':
                current_img_path = user.img_profile.path
                if os.path.exists(current_img_path):
                    os.remove(current_img_path)
                user.img_profile = 'uploads/default/defaultUser.jpg'
                user.save()
                return Response({'message': 'Profile image deleted and updated successfully.'}, status=status.HTTP_204_NO_CONTENT)
            else:
                if not user.img_profile:
                    user.img_profile = 'uploads/default/defaultUser.jpg'
                    user.save()
                    return Response({'error': 'User does not have a profile image. Therefore added default image'}, status=status.HTTP_404_NOT_FOUND)
                else:
                    return Response({'message': 'User already has default profile image.'}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({'error': f'Error deleting profile image: {str(e)}'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
