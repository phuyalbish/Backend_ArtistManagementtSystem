from rest_framework.views import APIView
from album.views.decorator import EnableDisableDecorator


class RecoverAlbum(APIView):
    @EnableDisableDecorator()
    def delete(self, request, albumid):
        return {"is_deleted": False}