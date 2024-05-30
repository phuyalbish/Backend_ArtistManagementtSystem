from rest_framework.views import APIView
from music.views.decorator import EnableDisableDecorator


class RecoverMusic(APIView):
    @EnableDisableDecorator()
    def delete(self, request, musicid):
        return {"is_deleted": False}