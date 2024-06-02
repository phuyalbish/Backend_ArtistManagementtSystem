from rest_framework.views import APIView
from music.views.decorator import EnableDisableDecorator
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from music.models import Like, Comment
from music.serializers import LikeSerializer
from rest_framework.permissions import AllowAny

class DeleteMusic(APIView):
    @EnableDisableDecorator()
    def delete(self, request, musicid):
       
        return {"is_deleted": True}
    


class DeleteLike(APIView):
     def delete(self, request, likeid):
        try:
            like = Like.objects.get(id=likeid)
        except Like.DoesNotExist:
            return Response({"detail": "Like not found"}, status=status.HTTP_404_NOT_FOUND)

        like.delete()
        return Response({"detail":"Unliked"}, status=status.HTTP_204_NO_CONTENT)
     
class DeleteComment(APIView):
     def delete(self, request, commentid):
        try:
            comment = Comment.objects.get(id=commentid)
        except Comment.DoesNotExist:
            return Response({"detail": "Comment not found"}, status=status.HTTP_404_NOT_FOUND)

        comment.delete()
        return Response({"detail":"Comment Deleted"}, status=status.HTTP_204_NO_CONTENT)