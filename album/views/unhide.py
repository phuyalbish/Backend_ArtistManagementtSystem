from rest_framework.views import APIView
from album.views.decorator import EnableDisableDecorator
from core.permissions import IsArtist,IsBand
from rest_framework.permissions import IsAuthenticated
from album.models import Album
from rest_framework.exceptions import PermissionDenied


class UnHideAlbum(APIView):
    permission_classes = [IsAuthenticated,  IsArtist | IsBand]
    @EnableDisableDecorator()
    def delete(self, request, albumid):
        music = Album.objects.get(id=albumid)
        if music.artist != request.user:
            raise PermissionDenied("You are not the owner of this album.")
        return {"is_hidden": False}