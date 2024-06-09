from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from genre.serializers import GenreSerializer
from rest_framework.permissions import IsAuthenticated
from core.permissions import IsStaff, IsSuperuser


class CreateGenre(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request):
        serializer = GenreSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=422)