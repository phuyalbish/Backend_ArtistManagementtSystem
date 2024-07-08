
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from album.serializers import AlbumSerializer, CommentSerializer
from album.models import Album, Comment
from rest_framework.permissions import AllowAny,IsAuthenticated
from core.views import StandardPagination
from core.permissions import  IsStaff, IsArtist


class GetAlbumManage(generics.ListAPIView):
    permission_classes = [IsAuthenticated, IsStaff | IsArtist]
    serializer_class = AlbumSerializer
    pagination_class = StandardPagination
    def get_queryset(self):
        return Album.objects.filter(is_deleted=False)

    
class GetDisabledAlbumManage(generics.ListAPIView):
    permission_classes = [IsAuthenticated, IsStaff]
    serializer_class = AlbumSerializer
    pagination_class = StandardPagination
    def get_queryset(self):
        return Album.objects.filter(is_disabled=True, is_deleted=False)

    
class GetDeletedAlbumManage(generics.ListAPIView):
    permission_classes = [IsAuthenticated, IsArtist]
    serializer_class = AlbumSerializer
    pagination_class = StandardPagination
    def get_queryset(self):
        return Album.objects.filter(artist=self.request.user.id, is_deleted=True)

class GetHiddenAlbumManage(generics.ListAPIView):
    permission_classes = [IsAuthenticated, IsArtist]
    serializer_class = AlbumSerializer
    pagination_class = StandardPagination
    def get_queryset(self):
        return Album.objects.filter(artist=self.request.user.id, is_deleted=False, is_hidden=True)


class GetLoggedInSpecificAlbumManage(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = AlbumSerializer
    pagination_class = StandardPagination
    def get_queryset(self):
        return Album.objects.filter(artist=self.request.user.id, is_deleted=False)

    


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

            user = request.user
            data = Album.objects.filter(artist=user.id, is_deleted=True)
            serializer = AlbumSerializer(data, many=True)
        except:
            return Response({"detail":"No Album in Artist"}, status=404)
        return Response(serializer.data)
    
    

class GetDisabledAlbum(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        try:
            datas = list(Album.objects.filter(is_disabled=True))
            serializer = AlbumSerializer(datas, many=True)
        except:
            return Response({"detail":"No Album Found"}, status=404)
        return Response(serializer.data)



class GetHiddenAlbum(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        try:    

            user = request.user
            data = Album.objects.filter(artist=user.id, is_deleted=False, is_hidden=True)
            serializer = AlbumSerializer(data, many=True)
        except:
            return Response({"detail":"No Album in Artist"}, status=404)
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