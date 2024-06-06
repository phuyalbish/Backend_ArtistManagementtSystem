from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from album.serializers import AlbumSerializer
from album.models import Album
from core.permissions import  IsArtist, IsBand
from rest_framework.permissions import IsAuthenticated


class CreateAlbum(APIView):
    permission_classes = [IsAuthenticated & (IsArtist | IsBand)]
    def post(self, request):
        data = request.data
        data['artist'] = request.user.id

        serializer = AlbumSerializer(data=data)
        if serializer.is_valid():
            if request.user != serializer.validated_data.get('artist'):
                return Response({"error": "You are not authorized to create an album for this artist or band."},
                                status=status.HTTP_403_FORBIDDEN)
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=422)