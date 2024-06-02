from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from user.serializers import UserSerializer
from user.models import Users
from rest_framework.permissions import AllowAny
from user.models import Artist
from user.serializers import ArtistSerializer
from rest_framework.permissions import IsAuthenticated
from core.permissions import IsStaff, IsSuperuser
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
        serializer = UserSerializer(instance=user, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class EditArtist(APIView):
    permission_classes = [IsAuthenticated]
    def patch(self, request, artistid):
        try:
            artist = Artist.objects.get(id=artistid)
        except Artist.DoesNotExist:
            return Response({"msg": "Artist not found"}, status=status.HTTP_404_NOT_FOUND)
        if artist.user != request.user and not request.user.is_staff and not request.user.is_superuser:
            raise PermissionDenied("You do not have permission to perform this action.")
        artist_data = request.data.copy()
        user_data = artist_data.pop('user', None)

        if user_data:
            user_serializer = UserSerializer(instance=artist.user, data=user_data, partial=True)
            if not user_serializer.is_valid():
                return Response(user_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        artist_serializer = ArtistSerializer(instance=artist, data=artist_data, partial=True)
        if artist_serializer.is_valid():
            artist_serializer.save()
            if user_data:
                user_serializer.save()
            return Response(artist_serializer.data, status=status.HTTP_200_OK)
        return Response(artist_serializer.errors, status=status.HTTP_400_BAD_REQUEST)