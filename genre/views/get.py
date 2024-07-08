
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from genre.serializers import GenreSerializer
from genre.models import Genre
from core.permissions import  IsStaff
from core.views import StandardPagination


class GetGenreManage(generics.ListAPIView):
    permission_classes = [IsStaff]
    serializer_class = GenreSerializer
    pagination_class = StandardPagination

    def get_queryset(self):
        return Genre.objects.filter(is_deleted=False)
    

class GetDeletedGenreManage(generics.ListAPIView):
    permission_classes = [IsStaff]
    serializer_class = GenreSerializer
    pagination_class = StandardPagination

    def get_queryset(self):
        return Genre.objects.filter(is_deleted=True)
    

class GetWeatherListView(APIView):
    def get(self, request, *args, **kwargs):
        weather = [weather[0] for weather in Genre.WEATHER]
        return Response({'weather': weather})
    
class GetGenre(APIView):
    def get(self, request):
        try:
            datas = list(Genre.objects.filter(is_deleted=False))
            serializer = GenreSerializer(datas, many=True)
        except:
            return Response({"detail":"No Genre Found"}, status=404)
        return Response(serializer.data)

class GetDeletedGenre(APIView):
    def get(self, request):
        try:
            datas = list(Genre.objects.filter(is_deleted=True))
            serializer = GenreSerializer(datas, many=True)
        except:
            return Response({"detail":"No Genre Found"}, status=404)
        return Response(serializer.data)

class GetGenreWithWeather(APIView):
    def get(self, request, weathername):
        try:
            genres = Genre.objects.filter(weather=weathername)
            serializer = GenreSerializer(genres, many=True)
            return Response(serializer.data)
        except Genre.DoesNotExist:
            return Response({"error": "Genre not found for this weather"}, status=404)



class GetGenreSpecific(APIView):
    def get(self, request, genreid):
        try:
            data = Genre.objects.get(pk=genreid, is_deleted=False)
            serializer = GenreSerializer(data, many=False)
        except:
            return Response({"detail":"No Genre Found"}, status=404)
        return Response(serializer.data)