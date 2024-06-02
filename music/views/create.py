from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
<<<<<<< HEAD
from music.serializers import MusicSerializer, LikeSerializer, CommentSerializer
=======
from music.serializers import MusicSerializer
from music.models import Music
from rest_framework.permissions import IsAuthenticated
from core.permissions import IsArtist,IsBand
>>>>>>> 1b4e5c6 (add permission for album, music, and user)


class CreateMusic(APIView):
    permission_classes = [IsAuthenticated & (IsArtist | IsBand)]
    def post(self, request):
        serializer = MusicSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=422)


class CreateLike(APIView):
    def post(self, request):
        serializer = LikeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=422)
        
class CreateComment(APIView):
    def post(self, request):
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=422)