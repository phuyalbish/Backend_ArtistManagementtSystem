from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from album.serializers import AlbumSerializer
from album.models import Album

class EditAlbum(APIView):
    def patch(self, request, albumid):
        try:
            user = Album.objects.get(id=albumid)
        except Album.DoesNotExist:
            return Response({"msg": "Album not found"}, status=status.HTTP_404_NOT_FOUND)
        serializer = AlbumSerializer(instance=user, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)