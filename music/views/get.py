
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from music.serializers import MusicSerializer, LikeSerializer, CommentSerializer
from music.models import Music, Like, Comment
from rest_framework.permissions import AllowAny, IsAuthenticated



class GetMusic(APIView):
    permission_classes = [AllowAny]
    def get(self, request):
        try:
            datas = list(Music.objects.filter(is_deleted=False))
            serializer = MusicSerializer(datas, many=True)
        except:
            return Response({"detail":"No Music Found"}, status=404)
        return Response(serializer.data)

    

class GetMusicSpecific(APIView):
    permission_classes = [AllowAny]
    def get(self, request, musicid):
        try:
            data = Music.objects.get(pk=musicid, is_deleted=False)
            serializer = MusicSerializer(data, many=False)
        except:
            return Response({"detail":"No Music Found"}, status=404)
        return Response(serializer.data)
    
class GetAlbumMusicSpecific(APIView):
    permission_classes = [AllowAny]
    def get(self, request, albumid):
        try:
            data = Music.objects.filter(album=albumid, is_deleted=False)
            serializer = MusicSerializer(data, many=True)
        except:
            return Response({"detail":"No Music in Album"}, status=404)
        return Response(serializer.data)

class GetLike(APIView):
    def get(self, request, musicid):
        try:
            data = Like.objects.get(music=musicid)
            serializer = LikeSerializer(data, many=True)
        except:
            return Response({"detail":"No Likes Yet"}, status=404)
        return Response(serializer.data)
    

    
class GetComment(APIView):
    def get(self, request, musicid):
        try:
            data = Comment.objects.filter(music=musicid)
            serializer = CommentSerializer(data, many=True)
        except:
            return Response({"detail":"No Comments Yet"}, status=404)
        return Response(serializer.data)
    
class GetArtistSpecificMusic(APIView):
    permission_classes = [AllowAny]
    def get(self, request, artistid):
        try:    
            data = Music.objects.filter(artist=artistid, is_deleted=False)
            serializer = MusicSerializer(data, many=True)
        except:
            return Response({"detail":"No Music in Artist"}, status=404)
        return Response(serializer.data)
    

class GetLoggedInSpecificMusic(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        try:    

            user = request.user
            data = Music.objects.filter(artist=user.id, is_deleted=False)
            serializer = MusicSerializer(data, many=True)
        except:
            return Response({"detail":"No Music in Artist"}, status=404)
        return Response(serializer.data)
    

