from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from music.serializers import MusicSerializer, LikeSerializer, CommentSerializer
from music.models import Music
from rest_framework.permissions import IsAuthenticated
from core.permissions import IsArtist,IsBand,IsNormalUser
from rest_framework.exceptions import PermissionDenied


class CreateMusic(APIView):
    permission_classes = [IsAuthenticated & (IsArtist | IsBand)]
    def post(self, request):
        data = request.data
        data['artist'] = request.user.id
        serializer = MusicSerializer(data=data)
        if serializer.is_valid():
            if request.data.get("artist")==request.user.id:
                serializer.save()
                return Response(serializer.data)
            else:
                raise PermissionDenied("You do not have permission to perform this action.")
        else:
            return Response(serializer.errors, status=422)


class CreateLike(APIView):
    permission_classes = [IsAuthenticated & (IsArtist | IsNormalUser)]
    def post(self, request):
        data = request.data
        data['user'] = request.user.id 
        serializer = LikeSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=422)
        
class CreateComment(APIView):
    permission_classes = [IsAuthenticated & (IsArtist | IsNormalUser)]
    def post(self, request):
        data = request.data
        data['user'] = request.user.id
        serializer = CommentSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=422)