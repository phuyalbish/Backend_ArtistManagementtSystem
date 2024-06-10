from rest_framework import status
from rest_framework.views import APIView
from user.models import Users
from rest_framework.response import Response
from customizeable.models import CustomTheme, CustomThemeSerializer
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
        
        user.selected_theme = theme
        user.save()

        return Response({'message': 'Theme selected successfully'}, status=status.HTTP_200_OK)
