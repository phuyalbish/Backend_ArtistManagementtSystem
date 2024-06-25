from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from music.serializers import MusicSerializer, CommentSerializer, CommentReplySerializer
from rest_framework.permissions import IsAuthenticated
from core.permissions import IsArtist,IsBand,IsNormalUser
from rest_framework.exceptions import PermissionDenied
from music.models import Music, Comment, Like, CommentLike, CommentReplyLike, CommentReply


class CreateMusic(APIView):
    permission_classes = [IsAuthenticated & (IsArtist | IsBand)]
    def post(self, request):
        data = request.data.copy() if isinstance(request.data, dict) else request.POST.copy()
        if 'artist' not in data:
            data['artist'] = request.user.id
            
        serializer = MusicSerializer(data=data)
        if serializer.is_valid():
            if data.get("artist")==request.user.id:
                serializer.save()
                return Response(serializer.data)
            else:
                raise PermissionDenied("You do not have permission to perform this action.")
        else:
            return Response(serializer.errors, status=422)



        
class CreateComment(APIView):
    permission_classes = [IsAuthenticated & (IsArtist | IsNormalUser)]
    def post(self, request):
        data = request.data.copy()
        data['user_id'] = request.user.id
        serializer = CommentSerializer(data=data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=422)
        



class CreateCommentReply(APIView):
    permission_classes = [IsAuthenticated & (IsArtist | IsNormalUser)]
    def post(self, request):
        data = request.data.copy()
        data['user_id'] = request.user.id
        serializer = CommentReplySerializer(data=data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=422)
        

        

class ToggleMusicLike(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request, musicid):
        user = request.user
        try:
            music = Music.objects.get(id=musicid)
        except Music.DoesNotExist:
            return Response({'error': 'Music not found'}, status=status.HTTP_404_NOT_FOUND)
        like, created = Like.objects.get_or_create(user=user, music=music)
        if not created:
            like.is_like = not like.is_like
            like.save()
            if like.is_like:
                return Response({'message': 'Music liked'}, status=status.HTTP_200_OK)
            else:
                return Response({'message': 'Music unliked'}, status=status.HTTP_200_OK)
        else:
            return Response({'message': 'Music liked'}, status=status.HTTP_201_CREATED)
        

class ToggleCommentLike(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request, commentid):
        user = request.user
        try:
            comment = Comment.objects.get(id=commentid)
        except Comment.DoesNotExist:
            return Response({'error': 'Comment not found'}, status=status.HTTP_404_NOT_FOUND)
        like, created = CommentLike.objects.get_or_create(user=user, comment=comment)
        if not created:
            like.is_like = not like.is_like
            like.save()
            if like.is_like:
                return Response({'message': 'Comment liked'}, status=status.HTTP_200_OK)
            else:
                return Response({'message': 'Comment unliked'}, status=status.HTTP_200_OK)
        else:
            return Response({'message': 'Comment liked'}, status=status.HTTP_201_CREATED)
        



class ToggleCommentReplyLike(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request, commentid):
        user = request.user
        try:
            comment = CommentReply.objects.get(id=commentid)
        except CommentReply.DoesNotExist:
            return Response({'error': 'Commentreply not found'}, status=status.HTTP_404_NOT_FOUND)
        like, created = CommentReplyLike.objects.get_or_create(user=user, comment=comment)
        if not created:
            like.is_like = not like.is_like
            like.save()
            if like.is_like:
                return Response({'message': 'Reply liked'}, status=status.HTTP_200_OK)
            else:
                return Response({'message': 'Reply unliked'}, status=status.HTTP_200_OK)
        else:
            return Response({'message': 'Reply liked'}, status=status.HTTP_201_CREATED)