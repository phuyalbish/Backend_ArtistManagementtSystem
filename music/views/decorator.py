from rest_framework.response import Response
from rest_framework import status
from music.models import Music
from music.serializers import MusicSerializer

class EnableDisableDecorator:
    def __call__(self, func):
        def wrapper(instance, request, musicid):
        
            try:
                music = Music.objects.get(id=musicid)
            except Music.DoesNotExist:
                return Response({"msg": "Music not found"}, status=status.HTTP_404_NOT_FOUND)
            toggledata = func(instance, request, musicid)
            serializer = MusicSerializer(instance=music, data=toggledata, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return wrapper