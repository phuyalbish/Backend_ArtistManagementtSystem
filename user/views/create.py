from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from user.serializers import UserSerializer,ArtistSerializer
from user.models import Users,Artist
from rest_framework.permissions import AllowAny


class CreateUser(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=422)
        
class CreateArtist(APIView):
    def post (self,request):
        user_serializer = UserSerializer(data=request.data.get('user'))
        artist_serializer = ArtistSerializer(data=request.data)
        user_serializer.is_valid()
        artist_serializer.is_valid()

        if user_serializer.is_valid() and artist_serializer.is_valid():
            user_instance = user_serializer.save()
            user_instance.is_artist = True
            user_instance.save()
            artist_data = {
                'user': user_instance,
                'stagename': request.data.get('stagename')
            }
            artist_instance = Artist.objects.create(**artist_data)
            return Response(artist_serializer.data, status=status.HTTP_201_CREATED)
        return Response(artist_serializer.errors, status=status.HTTP_400_BAD_REQUEST)