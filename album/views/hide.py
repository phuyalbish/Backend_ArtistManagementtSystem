from rest_framework.views import APIView
from music.views.decorator import EnableDisableDecorator
from core.permissions import IsArtist,IsBand
from rest_framework.permissions import IsAuthenticated
from album.models import Album
from rest_framework.exceptions import PermissionDenied


class HideAlbum(APIView):
    permission_classes = [IsAuthenticated,  IsArtist | IsBand]
    @EnableDisableDecorator()
    def delete(self, request, musicid):
        music = Album.objects.get(id=musicid)
        if music.artist != request.user:
            raise PermissionDenied("You are not the owner of this Album.")
        return {"is_hidden": True}