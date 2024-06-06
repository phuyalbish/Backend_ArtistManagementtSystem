from rest_framework.response import Response
from rest_framework import status
from genre.models import Genre
from genre.serializers import GenreSerializer

class EnableDisableDecorator:
    def __call__(self, func):
        def wrapper(instance, request, genreid):
        
            try:
                genre = Genre.objects.get(id=genreid)
            except Genre.DoesNotExist:
                return Response({"msg": "Genre not found"}, status=status.HTTP_404_NOT_FOUND)
            toggledata = func(instance, request, genreid)
            serializer = GenreSerializer(instance=genre, data=toggledata, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return wrapper