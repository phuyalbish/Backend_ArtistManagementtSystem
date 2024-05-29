from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response


class GetUser(APIView):
    def get(self, request):
            return Response({'data':'what the hell'})
