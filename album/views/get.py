
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from album.serializers import AlbumSerializer, CommentSerializer
from album.models import Album, Comment
from rest_framework.permissions import AllowAny,IsAuthenticated
from django.utils import timezone
from datetime import timedelta
from rest_framework import generics



class GetAlbum(APIView):
    permission_classes = [AllowAny]
    def get(self, request):
        try:
            datas = list(Album.objects.filter(is_hidden=False, is_deleted=False))
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


class GetArtistSpecificAlbum(APIView):
    permission_classes = [AllowAny]
    def get(self, request, artistid):
        try:    
            data = Album.objects.filter(artist=artistid, is_deleted=False, is_hidden=False)
            serializer = AlbumSerializer(data, many=True)
        except:
            return Response({"detail":"No Album in Artist"}, status=404)
        return Response(serializer.data)
class NewlyCreatedAlbumsView(generics.ListAPIView):
    serializer_class = AlbumSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        thirty_days_ago = timezone.now() - timedelta(days=30)
        return Album.objects.filter(created_at__gte=thirty_days_ago).order_by('-created_at')[:5]