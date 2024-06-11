
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from genre.serializers import GenreSerializer
from genre.models import Genre


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