from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from album.serializers import AlbumSerializer
from rest_framework.permissions import IsAuthenticated
from album.models import Album

class EditAlbum(APIView):
    permission_classes = [IsAuthenticated]
    def patch(self, request, albumid):
        try:
            user = Album.objects.get(id=albumid)
        except Album.DoesNotExist:
            return Response({"msg": "Album not found"}, status=status.HTTP_404_NOT_FOUND)
        serializer = AlbumSerializer(instance=user, data=request.data, partial=True)
        if serializer.is_valid():
             if request.user == user.artist or (user.band and request.user in user.band.members.all()):
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
             else:
                return Response({"error": "You don't have permission to update this album."}, status=status.HTTP_403_FORBIDDEN)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)