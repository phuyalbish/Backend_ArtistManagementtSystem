from rest_framework.views import APIView
from music.views.decorator import EnableDisableDecorator
from rest_framework.permissions import IsAuthenticated
from core.permissions import IsStaff, IsSuperuser


class RecoverMusic(APIView):
    permission_classes = [IsAuthenticated & (IsStaff | IsSuperuser)]
    @EnableDisableDecorator()
    def delete(self, request, musicid):
        return {"is_deleted": False}