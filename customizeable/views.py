from rest_framework import status
from rest_framework.views import APIView
from user.models import Users
from rest_framework.response import Response
from customizeable.models import CustomTheme, CustomThemeSerializer
from rest_framework.permissions import IsAuthenticated
from core.permissions import IsArtist

class SelectTheme(APIView):
    permission_classes = [IsAuthenticated & IsArtist]

    def post(self, request):
        user = request.user
        theme, created = CustomTheme.objects.get_or_create(user=user)
        
        data = request.data
        data['user'] = user.id

        if created:
            serializer = CustomThemeSerializer(instance=theme, data=data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            serializer = CustomThemeSerializer(instance=theme, data=data, partial=True)
            if serializer.is_valid():
                # if user == user.is_artist | True:
                    serializer.save()
                    return Response(serializer.data, status=status.HTTP_200_OK)
                # else:
                #     return Response({"error": "You don't have permission to update this theme."}, status=status.HTTP_403_FORBIDDEN)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)