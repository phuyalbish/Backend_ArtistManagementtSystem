from rest_framework.views import APIView
from music.views.decorator import EnableDisableDecorator
from core.permissions import IsSuperuser,IsStaff
from rest_framework.permissions import IsAuthenticated


class EnableMusic(APIView):
    permission_classes = [IsAuthenticated,  IsStaff | IsSuperuser]
    @EnableDisableDecorator()
    def delete(self, request, musicid):
        return {"is_disabled": False}