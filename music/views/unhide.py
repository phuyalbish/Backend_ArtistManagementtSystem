from rest_framework.views import APIView
from music.views.decorator import EnableDisableDecorator
from core.permissions import IsArtist,IsBand
from rest_framework.permissions import IsAuthenticated
from music.models import Music
from rest_framework.exceptions import PermissionDenied


class UnHideMusic(APIView):
    permission_classes = [IsAuthenticated,  IsArtist | IsBand]
    @EnableDisableDecorator()
    def delete(self, request, musicid):
        music = Music.objects.get(id=musicid)
        if music.artist != request.user:
            raise PermissionDenied("You are not the owner of this music.")
        return {"is_hidden": False}