from rest_framework.views import APIView
from album.views.decorator import EnableDisableDecorator


class DisableAlbum(APIView):
    @EnableDisableDecorator()
    def delete(self, request, albumid):
       
        return {"is_disabled": True}