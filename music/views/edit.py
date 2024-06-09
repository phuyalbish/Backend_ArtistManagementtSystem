from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from music.serializers import MusicSerializer, CommentSerializer
from music.models import Music, Comment
from rest_framework.permissions import IsAuthenticated
from core.permissions import IsArtist, IsBand
from rest_framework.exceptions import PermissionDenied


class EditMusic(APIView):
    permission_classes = [IsAuthenticated & IsArtist]

    def patch(self, request, musicid):
        try:
            user = Music.objects.get(id=musicid)
        except Music.DoesNotExist:
            return Response({"msg": "Music not found"}, status=status.HTTP_404_NOT_FOUND)
        serializer = MusicSerializer(instance=user, data=request.data, partial=True)
        if serializer.is_valid():
            if request.user == user.artist or (user.band and request.user in user.band.members.all()):
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                return Response({"error": "You don't have permission to update this song."}, status=status.HTTP_403_FORBIDDEN)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class EditComment(APIView):
    def patch(self, request, commentid):
        try:
            comment = Comment.objects.get(id=commentid)
        except Comment.DoesNotExist:
            return Response({"msg": "Comment not found"}, status=status.HTTP_404_NOT_FOUND)
        serializer = CommentSerializer(instance=comment, data=request.data, partial=True)
        if serializer.is_valid():
            if comment.user != request.user:
                raise PermissionDenied("You are not the owner of this comment.")
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    