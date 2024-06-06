from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from band.models import BandMember

class RemoveBandMember(APIView):
    permission_classes = [IsAuthenticated]

    def delete(self, request, memberid):
        try:
            member = BandMember.objects.get(id=memberid)
        except BandMember.DoesNotExist:
            return Response({"detail": "Band member not found"}, status=status.HTTP_404_NOT_FOUND)

        member.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)