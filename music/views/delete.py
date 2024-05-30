from rest_framework.views import APIView
from music.views.decorator import EnableDisableDecorator


class DeleteMusic(APIView):
    @EnableDisableDecorator()
    def delete(self, request, musicid):
       
        return {"is_deleted": True}