from rest_framework.views import APIView
from band.views.decorator import EnableDisableDecorator


class DeleteBand(APIView):
    @EnableDisableDecorator()
    def delete(self, request, bandid):
       
        return {"is_deleted": True}