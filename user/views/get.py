from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from user.serializers import UserSerializer
from user.models import Users
from rest_framework.permissions import AllowAny
from rest_framework.permissions import IsAuthenticated

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
            datas = Users.objects.filter(is_deleted=False, is_artist=True, is_superuser=False)
            artist_serializer = UserSerializer(datas, many=True)
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
            data = Users.objects.get(pk=artistid, is_artist=True, user__is_deleted=False)
            serializer = Users(data, many=False)
        except:
            return Response({"detail":"No Artist Found"}, status=404)
        return Response(serializer.data)
        
    

class GetLoggedInUser(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        serializer = UserSerializer(user)
        return Response(serializer.data)