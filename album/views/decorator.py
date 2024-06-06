from rest_framework.response import Response
from rest_framework import status
from album.models import Album
from album.serializers import AlbumSerializer

class EnableDisableDecorator:
    def __call__(self, func):
        def wrapper(instance, request, albumid):
        
            try:
                album = Album.objects.get(id=albumid)
            except Album.DoesNotExist:
                return Response({"msg": "Album not found"}, status=status.HTTP_404_NOT_FOUND)
            toggledata = func(instance, request, albumid)
            serializer = AlbumSerializer(instance=album, data=toggledata, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return wrapper