import django
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from customizeable.models import CustomTheme, CustomThemeSerializer
from core.permissions import  IsSuperuser, IsStaff, IsArtist


class GetTheme(APIView):
    permission_classes = [IsAuthenticated,  IsSuperuser | IsArtist | IsStaff]
    def get(self, request):
        try:
            datas = CustomTheme.objects.filter(is_deleted=False)
            serializer = CustomThemeSerializer(datas, many=True)
        except:
            return Response({"detail":"No Theme Found"}, status=404)
        return Response(serializer.data, status=status.HTTP_200_OK)
    

class GetSpecificTheme(APIView):
    permission_classes = [IsAuthenticated,  IsSuperuser | IsArtist | IsStaff]
    def get(self, request, themeid):
        try:
            datas = CustomTheme.objects.get(is_deleted=False, pk=themeid)
            serializer = CustomThemeSerializer(datas, many=False)
        except:
            return Response({"detail":"No Theme Found"}, status=404)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
class GetDeletedTheme(APIView):
    permission_classes = [IsAuthenticated,  IsSuperuser | IsArtist | IsStaff]
    def get(self, request):
        try:
            datas = CustomTheme.objects.filter(is_deleted=True)
            serializer = CustomThemeSerializer(datas, many=True)
        except:
            return Response({"detail":"No Theme Found"}, status=404)
        return Response(serializer.data, status=status.HTTP_200_OK)

