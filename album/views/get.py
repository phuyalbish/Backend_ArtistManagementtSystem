
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from album.serializers import AlbumSerializer
from album.models import Album
from rest_framework.permissions import AllowAny


class GetAlbum(APIView):
    permission_classes = [AllowAny]
    def get(self, request):
        try:
            datas = list(Album.objects.filter(is_deleted=False))
            serializer = AlbumSerializer(datas, many=True)
        except:
            return Response({"detail":"No Album Found"}, status=404)
        return Response(serializer.data)

    

class GetAlbumSpecific(APIView):
    permission_classes = [AllowAny]
    def get(self, request, albumid):
        try:
            data = Album.objects.get(pk=albumid, is_deleted=False)
            serializer = AlbumSerializer(data, many=False)
        except:
            return Response({"detail":"No Album Found"}, status=404)
        return Response(serializer.data)