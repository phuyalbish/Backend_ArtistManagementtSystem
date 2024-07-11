from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from album.serializers import AlbumSerializer, CommentSerializer, CommentReplySerializer
from album.models import Album,  Comment, Like, CommentLike, CommentReplyLike, CommentReply
from core.permissions import  IsArtist, IsBand, IsNormalUser
from rest_framework.permissions import IsAuthenticated


class CreateAlbum(APIView):
    permission_classes = [IsAuthenticated & (IsArtist | IsBand)]
    def post(self, request):
        data = request.data.copy() if isinstance(request.data, dict) else request.POST.copy()
        if 'artist' not in data:
            data['artist'] = request.user.id

        serializer = AlbumSerializer(data=data)
        if serializer.is_valid():
            if request.user != serializer.validated_data.get('artist'):
                return Response({"error": "You are not authorized to create an album for this artist or band."},
                                status=status.HTTP_403_FORBIDDEN)
            serializer.save()
            return Response(serializer.data)
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
        

        

class ToggleAlbumLike(APIView):
    permission_classes = [IsAuthenticated & (IsArtist | IsNormalUser)]
    def post(self, request, albumid):
        user = request.user
        try:
            album = Album.objects.get(id=albumid)
        except Album.DoesNotExist:
            return Response({'error': 'Music not found'}, status=status.HTTP_404_NOT_FOUND)
        like, created = Like.objects.get_or_create(user=user, album=album)
        if not created:
            like.is_like = not like.is_like
            like.save()
            if like.is_like:
                return Response({'message': 'Album liked'}, status=status.HTTP_200_OK)
            else:
                return Response({'message': 'Album unliked'}, status=status.HTTP_200_OK)
        else:
            return Response({'message': 'Album liked'}, status=status.HTTP_201_CREATED)
        

class ToggleCommentLike(APIView):
    permission_classes = [IsAuthenticated & (IsArtist | IsNormalUser)]
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
    permission_classes = [IsAuthenticated & (IsArtist | IsNormalUser)]
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