from rest_framework.response import Response
from rest_framework import status
from band.models import Band
from band.serializers import BandSerializer

class EnableDisableDecorator:
    def __call__(self, func):
        def wrapper(instance, request, bandid, *args, **kwargs):
            try:
                band = Band.objects.get(id=bandid)
            except Band.DoesNotExist:
                return Response({"detail": "Band not found"}, status=status.HTTP_404_NOT_FOUND)
            
            toggledata = func(instance, request, bandid, *args, **kwargs)
            
            serializer = BandSerializer(band, data=toggledata, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return wrapper