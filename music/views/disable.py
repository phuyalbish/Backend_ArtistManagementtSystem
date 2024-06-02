from rest_framework.views import APIView
from music.views.decorator import EnableDisableDecorator


class DisableMusic(APIView):
    @EnableDisableDecorator()
    def delete(self, request, musicid):
       
        return {"is_disabled": True}