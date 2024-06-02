
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from band.serializers import BandSerializer
from band.models import Band, BandMember
from band.serializers import BandMemberSerializer

class GetBand(APIView):
    def get(self, request):
        try:
            bands = Band.objects.filter(is_deleted=False)
            if not bands:
                return Response({"detail": "No Band Found"}, status=status.HTTP_404_NOT_FOUND)
            serializer = BandSerializer(bands, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"detail": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class GetBandSpecific(APIView):
    def get(self, request, bandid):
        try:
            band = Band.objects.get(pk=bandid, is_deleted=False)
            serializer = BandSerializer(band)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Band.DoesNotExist:
            return Response({"detail": "No Band Found"}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({"detail": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class GetBandMemberList(APIView):
    def get(self, request, bandid):
        try:
            bandmembers = BandMember.objects.filter(band_id=bandid)
            serializer = BandMemberSerializer(bandmembers, many=True)
        except BandMember.DoesNotExist:
            return Response({"detail": "No Band Member Found"}, status=status.HTTP_404_NOT_FOUND)
        return Response(serializer.data)
