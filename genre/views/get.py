
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from genre.serializers import GenreSerializer
from genre.models import Genre


class GetGenre(APIView):
    def get(self, request):
        try:
            datas = list(Genre.objects.filter(is_deleted=False))
            serializer = GenreSerializer(datas, many=True)
        except:
            return Response({"detail":"No Genre Found"}, status=404)
        return Response(serializer.data)

    

class GetGenreSpecific(APIView):
    def get(self, request, genreid):
        try:
            data = Genre.objects.get(pk=genreid, is_deleted=False)
            serializer = GenreSerializer(data, many=False)
        except:
            return Response({"detail":"No Genre Found"}, status=404)
        return Response(serializer.data)