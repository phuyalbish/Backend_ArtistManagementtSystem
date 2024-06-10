from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from customizeable.models import CustomTheme, CustomThemeSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import PermissionDenied



class EditTheme(APIView):
    permission_classes = [IsAuthenticated]
    def patch(self, request,themeid):
        try:
            theme = CustomTheme.objects.get(id=themeid)
        except CustomTheme.DoesNotExist:
            return Response({"msg": "Theme not found"}, status=status.HTTP_404_NOT_FOUND)
        serializer = CustomThemeSerializer(instance=theme, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)