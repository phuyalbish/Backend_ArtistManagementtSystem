from rest_framework.views import APIView
from user.views.decoraor import EnableDisableDecorator


class RecoverUser(APIView):
    @EnableDisableDecorator()
    def delete(self, request, userid):
        return {"is_deleted": False}
