from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from album.serializers import AlbumSerializer
from album.models import Album


class CreateAlbum(APIView):
     def post(self, request):
        data= request.data
        data['artist']=request.user.id
        serializer = AlbumSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=422)