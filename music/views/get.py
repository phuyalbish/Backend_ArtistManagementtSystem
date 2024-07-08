
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from music.serializers import MusicSerializer, CommentSerializer
from album.serializers import AlbumSerializer
from music.models import Music, Like, Comment
from album.models import Album
from core.views import StandardPagination
from core.permissions import  IsStaff, IsArtist
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser
from genre.models import Genre
import random
from rest_framework import generics



class GetMusicManage(generics.ListAPIView):
    permission_classes = [IsAuthenticated, IsStaff | IsArtist]
    serializer_class = MusicSerializer
    pagination_class = StandardPagination
    def get_queryset(self):
        return Music.objects.filter(is_deleted=False)

    
class GetDisabledMusicManage(generics.ListAPIView):
    permission_classes = [IsAuthenticated, IsStaff]
    serializer_class = MusicSerializer
    pagination_class = StandardPagination
    def get_queryset(self):
        return Music.objects.filter(is_disabled=True, is_deleted=False)

    
class GetDeletedMusicManage(generics.ListAPIView):
    permission_classes = [IsAuthenticated, IsArtist]
    serializer_class = MusicSerializer
    pagination_class = StandardPagination
    def get_queryset(self):
        return Music.objects.filter(artist=self.request.user.id, is_deleted=True)

class GetHiddenMusicManage(generics.ListAPIView):
    permission_classes = [IsAuthenticated, IsArtist]
    serializer_class = MusicSerializer
    pagination_class = StandardPagination
    def get_queryset(self):
        return Music.objects.filter(artist=self.request.user.id, is_deleted=False, is_hidden=True)


class GetLoggedInSpecificMusicManage(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = MusicSerializer
    pagination_class = StandardPagination
    def get_queryset(self):
        return Music.objects.filter(artist=self.request.user.id, is_deleted=False)

    



class GetMusic(APIView):
    permission_classes = [AllowAny]
    def get(self, request):
        try:
            datas = list(Music.objects.filter(is_disabled=False,is_deleted=False,is_hidden=False))
            serializer = MusicSerializer(datas, many=True)
        except:
            return Response({"detail":"No Music Found"}, status=404)
        return Response(serializer.data)




class GetAdminMusic(APIView):
    permission_classes = [IsAuthenticated & IsAdminUser]
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
            data = Music.objects.filter(is_disabled=False,album=albumid, is_deleted=False, is_hidden=False)
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
            data = Music.objects.filter(is_disabled=False, artist=artistid, is_deleted=False, is_hidden=False)
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
    




    

class GetDisabledMusic(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        try:
            datas = list(Music.objects.filter(is_disabled=True))
            serializer = MusicSerializer(datas, many=True)
        except:
            return Response({"detail":"No Music Found"}, status=404)
        return Response(serializer.data)



class GetHiddenMusic(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        try:    

            user = request.user
            data = Music.objects.filter(artist=user.id, is_deleted=False, is_hidden=True)
            serializer = MusicSerializer(data, many=True)
        except:
            return Response({"detail":"No Music in Artist"}, status=404)
        return Response(serializer.data)
    

    
class GetDeletedMusic(APIView):
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
        music_from_weather = Music.objects.filter(is_disabled=False, genre__in=genres, is_hidden=False, is_deleted=False)
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
        music_from_weather = Music.objects.filter(is_disabled=False, genre=genreid, is_hidden=False, is_deleted=False)
        serializer = MusicSerializer(music_from_weather, many=True, )
        serialized_music = serializer.data
        return Response(serialized_music)
    
class GetAllMusicWithGenre(APIView):
    def get(self, request):
        music_with_genre = Music.objects.exclude(genre=None, is_hidden=True, is_deleted=True) 
        serializer = MusicSerializer(music_with_genre, many=True)
        return Response(serializer.data)


class UserLikedMusicList(generics.ListAPIView):
    serializer_class = MusicSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        liked_music_ids = Like.objects.filter(user=user, is_like=True).values_list('music_id', flat=True)
        return Music.objects.filter(id__in=liked_music_ids, is_deleted=False)



class UserLikedAlbumList(generics.ListAPIView):
    serializer_class = AlbumSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        liked_album_ids = Like.objects.filter(user=user, is_like=True).values_list('id', flat=True)
        return Album.objects.filter(id__in=liked_album_ids, is_deleted=False)