
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from music.serializers import MusicSerializer, LikeSerializer, CommentSerializer, CommentReplySerializer,CommentLikeSerializer, CommentReplyLikeSerializer
from music.models import Music, Like, Comment, CommentLike, CommentReply, CommentReplyLike
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser
from genre.models import Genre
import random

class GetMusic(APIView):
    permission_classes = [AllowAny]
    def get(self, request):
        try:
            datas = list(Music.objects.filter(is_deleted=False,is_hidden=False))
            serializer = MusicSerializer(datas, many=True)
        except:
            return Response({"detail":"No Music Found"}, status=404)
        return Response(serializer.data)

class GetDeletedMusic(APIView):
    permission_classes = [AllowAny & IsAuthenticated]
    def get(self, request):
        try:
            datas = list(Music.objects.filter(is_deleted=True))
            serializer = MusicSerializer(datas, many=True)
        except:
            return Response({"detail":"No Deleted Music Found"}, status=404)
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


class GetComment(APIView):
    permission_classes = [AllowAny]
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
    
class GetLoggedInSpecificDeletedMusic(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        try:    
            user = request.user
            data = Music.objects.filter(artist=user.id, is_deleted=True)
            serializer = MusicSerializer(data, many=True)
        except:
            return Response({"detail":"No Music in Artist"}, status=404)
        return Response(serializer.data)
    
class GetMusicFromGenreWeather(APIView):
    permission_classes = [AllowAny]
    def get(self, request, weathername):
        try:
            genres = Genre.objects.filter(weather=weathername)
        except Genre.DoesNotExist:
            return Response({"error": "Weather not found"}, status=404)
        music_from_weather = Music.objects.filter(genre__in=genres)
        music_list = list(music_from_weather)
        random.shuffle(music_list)
        music_list = music_list[:5]
        serializer = MusicSerializer(music_list, many=True)
        serialized_music = serializer.data
        return Response(serialized_music)
    

class MusicCountView(APIView):
    def get(self, request, *args, **kwargs):
        total_music = Music.objects.count()
        return Response({'total_music': total_music})

class GetMusicFromGenre(APIView):
    permission_classes = [AllowAny]
    def get(self, request, genreid):
        music_from_weather = Music.objects.filter(genre=genreid)
        serializer = MusicSerializer(music_from_weather, many=True)
        serialized_music = serializer.data
        return Response(serialized_music)
    
class GetAllMusicWithGenre(APIView):
    def get(self, request):
        music_with_genre = Music.objects.exclude(genre=None)
        serializer = MusicSerializer(music_with_genre, many=True)
        return Response(serializer.data)

