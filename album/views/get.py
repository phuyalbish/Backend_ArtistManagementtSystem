
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from album.serializers import AlbumSerializer, CommentSerializer
from album.models import Album, Comment
from rest_framework.permissions import AllowAny,IsAuthenticated


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
    
class GetLoggedInSpecificAlbum(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        try:    

            user = request.user
            data = Album.objects.filter(artist=user.id, is_deleted=False)
            serializer = AlbumSerializer(data, many=True)
        except:
            return Response({"detail":"No Music in Artist"}, status=404)
        return Response(serializer.data)
    
class AlbumCountView(APIView):
    def get(self, request, *args, **kwargs):
        total_albums = Album.objects.count()
        return Response({'total_albums': total_albums})



class GetComment(APIView):
    permission_classes = [AllowAny]
    def get(self, request, albumid):
        try:
            data = Comment.objects.filter(music=albumid)
            serializer = CommentSerializer(data, many=True)
        except:
            return Response({"detail":"No Comments Yet"}, status=404)
        return Response(serializer.data)
    

class GetDeletedAlbum(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        try:
            datas = list(Album.objects.filter(is_deleted=True))
            serializer = AlbumSerializer(datas, many=True)
        except:
            return Response({"detail":"No Album Found"}, status=404)
        return Response(serializer.data)


class GetLoggedInSpecificDeletedAlbum(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        try:    

            user = request.user
            data = Album.objects.filter(artist=user.id, is_deleted=True)
            serializer = AlbumSerializer(data, many=True)
        except:
            return Response({"detail":"No Music in Artist"}, status=404)
        return Response(serializer.data)

