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
        serializer = AlbumSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=422)