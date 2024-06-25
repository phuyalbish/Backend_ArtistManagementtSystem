from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from customizeable.models import CustomTheme
from user.models import Users
from user.serializers import UserSerializer
from rest_framework.permissions import IsAuthenticated
from core.permissions import IsArtist

class SelectTheme(APIView):
    permission_classes = [IsAuthenticated & IsArtist]
    def patch(self, request, themeid):
        user = request.user
        try:
            theme = CustomTheme.objects.get(id=themeid)
        except CustomTheme.DoesNotExist:
            return Response({'error': 'Theme not found'}, status=status.HTTP_404_NOT_FOUND)

        user.theme = theme
        user.save()

        return Response({'message': 'Theme selected successfully'}, status=status.HTTP_200_OK)


class UnSelectTheme(APIView):
    permission_classes = [IsAuthenticated & IsArtist]
    def patch(self, request):
        user = Users.objects.get(id=request.user.id)
        user.theme = None
        serializer = UserSerializer(instance=user, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)