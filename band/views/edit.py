from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from band.serializers import BandSerializer
from band.models import Band



class EditBand(APIView):
    def patch(self, request,bandid):
        try:
            band = Band.objects.get(id=bandid)
        except Band.DoesNotExist:
            return Response({"msg": "Band not found"}, status=status.HTTP_404_NOT_FOUND)
        serializer = BandSerializer(instance=band, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)