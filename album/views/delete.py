from rest_framework.views import APIView
from album.views.decorator import EnableDisableDecorator


class DeleteAlbum(APIView):
    @EnableDisableDecorator()
    def delete(self, request, albumid):
       
        return {"is_deleted": True}