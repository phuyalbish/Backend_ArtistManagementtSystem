from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from user.serializers import UserSerializer
from user.models import Users
from rest_framework.permissions import AllowAny


class GetUser(APIView):
    def get(self, request):
        try:
            datas = Users.objects.filter(is_deleted=False, is_superuser=False)
            serializer = UserSerializer(datas, many=True)
        except:
            return Response({"detail":"No User Found"}, status=404)
        return Response(serializer.data)

    

class GetUserSpecific(APIView):
    def get(self, request, userid):
        try:
            data = Users.objects.get(pk=userid, is_deleted=False)
            serializer = UserSerializer(data, many=False)
        except:
            return Response({"detail":"No User Found"}, status=404)
        return Response(serializer.data)

 
        
    
    
    
    

