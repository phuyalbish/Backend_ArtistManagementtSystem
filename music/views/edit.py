from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from music.serializers import MusicSerializer
from music.models import Music

class EditMusic(APIView):
    def patch(self, request, musicid):
        try:
            user = Music.objects.get(id=musicid)
        except Music.DoesNotExist:
            return Response({"msg": "Music not found"}, status=status.HTTP_404_NOT_FOUND)
        serializer = MusicSerializer(instance=user, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)