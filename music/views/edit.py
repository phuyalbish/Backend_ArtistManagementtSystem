from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
<<<<<<< HEAD
from music.serializers import MusicSerializer, CommentSerializer
from music.models import Music, Comment
=======
from music.serializers import MusicSerializer
from music.models import Music
from rest_framework.permissions import IsAuthenticated
from core.permissions import IsArtist, IsBand, IsOwner

>>>>>>> 1b4e5c6 (add permission for album, music, and user)

class EditMusic(APIView):
    permission_classes = [IsAuthenticated & (IsArtist | IsBand) & IsOwner]
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
    
class EditComment(APIView):
    def patch(self, request, commentid):
        try:
            user = Comment.objects.get(id=commentid)
        except Comment.DoesNotExist:
            return Response({"msg": "Comment not found"}, status=status.HTTP_404_NOT_FOUND)
        serializer = CommentSerializer(instance=user, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)