from rest_framework.views import APIView
from album.views.decorator import EnableDisableDecorator
from rest_framework.permissions import IsAuthenticated
from core.permissions import IsArtist,IsBand
from music.models import Album
from rest_framework.exceptions import PermissionDenied

class RecoverAlbum(APIView):
    permission_classes = [IsAuthenticated & (IsArtist | IsBand)]
    @EnableDisableDecorator()
    def delete(self, request, albumid):
        album = Album.objects.get(id=albumid)
        if request.user != album.artist:
            raise PermissionDenied("You do not have permission to delete this album")
        return {"is_deleted": False}