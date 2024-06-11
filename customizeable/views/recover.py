from rest_framework.views import APIView
from customizeable.views.decorator import EnableDisableDecorator
from rest_framework.permissions import IsAuthenticated
from customizeable.models import CustomTheme
from core.permissions import  IsSuperuser, IsStaff, IsArtist



class RecoverTheme(APIView):
    permission_classes = [IsAuthenticated,  IsSuperuser | IsArtist | IsStaff]
    @EnableDisableDecorator()
    def delete(self, request, themeid):
        return {"is_deleted": False}

