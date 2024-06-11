from rest_framework.views import APIView
from customizeable.views.decorator import EnableDisableDecorator
from rest_framework.permissions import IsAuthenticated
from core.permissions import  IsSuperuser, IsStaff, IsArtist



class DeleteTheme(APIView):
    permission_classes = [IsAuthenticated,  IsSuperuser | IsArtist | IsStaff]
    @EnableDisableDecorator()
    def delete(self, request, themeid):
        return {"is_deleted": True}

