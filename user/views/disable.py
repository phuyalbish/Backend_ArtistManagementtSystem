from rest_framework.views import APIView
from user.views.decorator import EnableDisableDecorator


class DisableUser(APIView):
    @EnableDisableDecorator()
    def delete(self, request, userid):
       
        return {"is_disabled": True}