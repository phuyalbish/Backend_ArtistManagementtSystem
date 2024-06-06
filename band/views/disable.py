from rest_framework.views import APIView
from band.views.decorator import EnableDisableDecorator


class DisableBand(APIView):
    @EnableDisableDecorator()
    def delete(self, request, bandid):
       
        return {"is_disabled": True}