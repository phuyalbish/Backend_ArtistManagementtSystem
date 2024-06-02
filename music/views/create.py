from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from music.serializers import MusicSerializer, LikeSerializer, CommentSerializer
from music.models import Music
from rest_framework.permissions import IsAuthenticated
from core.permissions import IsArtist,IsBand


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