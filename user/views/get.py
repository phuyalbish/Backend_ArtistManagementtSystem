from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from user.serializers import UserSerializer,ArtistSerializer
from user.models import Users,Artist
from rest_framework.permissions import AllowAny


class GetUser(APIView):
    def get(self, request):
        try:
            datas = Users.objects.filter(is_deleted=False, is_superuser=False)
            serializer = UserSerializer(datas, many=True)
        except:
            return Response({"detail":"No User Found"}, status=404)
        return Response(serializer.data)

class GetArtist(APIView):
    def get(self, request):
        try:
            datas = Artist.objects.filter(user__is_deleted=False,user__is_superuser=False)
            artist_serializer = ArtistSerializer(datas, many=True)
        except:
            return Response({"detail":"No Artist Found"}, status=404)
        return Response(artist_serializer.data, status=status.HTTP_200_OK)

class GetUserSpecific(APIView):
    def get(self, request, userid):
        try:
            data = Users.objects.get(pk=userid, is_deleted=False)
            serializer = UserSerializer(data, many=False)
        except:
            return Response({"detail":"No User Found"}, status=404)
        return Response(serializer.data)

class GetArtistSpecific(APIView):
    def get(self, request, artistid):
        try:
            data = Artist.objects.get(pk=artistid, user__is_deleted=False)
            serializer = ArtistSerializer(data, many=False)
        except:
            return Response({"detail":"No User Found"}, status=404)
        return Response(serializer.data)
        
    
    
    
    

