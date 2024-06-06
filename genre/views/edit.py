from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from genre.serializers import GenreSerializer
from genre.models import Genre
from rest_framework.permissions import IsAuthenticated
from core.permissions import IsStaff, IsSuperuser

class EditGenre(APIView):
    permission_classes = [IsAuthenticated & (IsStaff | IsSuperuser)]
    def patch(self, request, genreid):
        try:
            user = Genre.objects.get(id=genreid)
        except Genre.DoesNotExist:
            return Response({"msg": "Genre not found"}, status=status.HTTP_404_NOT_FOUND)
        serializer = GenreSerializer(instance=user, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)