from rest_framework.views import APIView
from music.views.decorator import EnableDisableDecorator


class EnableUser(APIView):
    @EnableDisableDecorator()
    def delete(self, request, userid):
       
        return {"is_disabled": False}