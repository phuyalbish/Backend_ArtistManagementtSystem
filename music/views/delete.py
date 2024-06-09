from rest_framework.views import APIView
from music.views.decorator import EnableDisableDecorator
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from music.models import Comment,Music, CommentReply
from rest_framework.permissions import IsAuthenticated
from core.permissions import IsArtist,IsNormalUser,IsBand
from rest_framework.exceptions import PermissionDenied


class DeleteMusic(APIView):
    permission_classes = [IsAuthenticated & (IsArtist | IsBand)]
    @EnableDisableDecorator()
    def delete(self, request, musicid):
        music = Music.objects.get(id=musicid)
        if music.artist != request.user:
            raise PermissionDenied("You are not the owner of this music.")
        return {"is_deleted": True}
    
     
class DeleteComment(APIView):
     permission_classes = [IsAuthenticated & (IsArtist | IsNormalUser)]
     def delete(self, request, commentid):
        try:
            comment = Comment.objects.get(id=commentid)
        except Comment.DoesNotExist:
            return Response({"detail": "Comment not found"}, status=status.HTTP_404_NOT_FOUND)
        if comment.user != request.user:
            raise PermissionDenied("You are not the owner of this comment.")
        comment.delete()
        return Response({"detail":"Comment Deleted"}, status=status.HTTP_204_NO_CONTENT)
     
     
class DeleteCommentReply(APIView):
     permission_classes = [IsAuthenticated & (IsArtist | IsNormalUser)]
     def delete(self, request, commentid):
        try:
            comment = CommentReply.objects.get(id=commentid)
        except CommentReply.DoesNotExist:
            return Response({"detail": "Reply not found"}, status=status.HTTP_404_NOT_FOUND)
        if comment.user != request.user:
            raise PermissionDenied("You are not the owner of this reply.")
        comment.delete()
        return Response({"detail":"Reply Deleted"}, status=status.HTTP_204_NO_CONTENT)