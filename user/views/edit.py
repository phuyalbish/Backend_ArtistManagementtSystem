from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from user.serializers import UserSerializer
from user.models import Users
from rest_framework.permissions import AllowAny
from user.models import Artist
from user.serializers import ArtistSerializer



class EditUser(APIView):
    def patch(self, request,userid):
        try:
            user = Users.objects.get(id=userid)
        except Users.DoesNotExist:
            return Response({"msg": "User not found"}, status=status.HTTP_404_NOT_FOUND)
        serializer = UserSerializer(instance=user, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class EditArtist(APIView):
    def patch(self, request, artistid):
        try:
            artist = Artist.objects.get(id=artistid)
        except Artist.DoesNotExist:
            return Response({"msg": "Artist not found"}, status=status.HTTP_404_NOT_FOUND)

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