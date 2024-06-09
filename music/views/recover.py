from rest_framework.views import APIView
from music.views.decorator import EnableDisableDecorator
from rest_framework.permissions import IsAuthenticated
from core.permissions import IsArtist,IsBand, IsSuperuser
from rest_framework.exceptions import PermissionDenied
from music.models import Music


class RecoverMusic(APIView):
    permission_classes = [IsAuthenticated & (IsArtist | IsBand | IsSuperuser)]
    @EnableDisableDecorator()
    def delete(self, request, musicid):
        music = Music.objects.get(id=musicid)
        # if music.artist != request.user or not request.user.is_staff:
        #     raise PermissionDenied("You are not the owner of this music.")
        return {"is_deleted": False}