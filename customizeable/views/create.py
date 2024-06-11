from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from customizeable.models import CustomThemeSerializer
from rest_framework.permissions import IsAuthenticated
from core.permissions import  IsSuperuser, IsStaff


class CreateTheme(APIView):
    # permission_classes = [IsAuthenticated & (IsSuperuser | IsStaff)]
    def post(self, request):
        serializer = CustomThemeSerializer(data=request.data)
        if serializer.is_valid():
             serializer.save()
        #     if not request.user.is_superuser:
        #         raise PermissionDenied("You do not have permission to perform this action.")
        else:
                return Response(serializer.errors, status=422)
        return Response(serializer.data)
        