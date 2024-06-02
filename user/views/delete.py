from rest_framework.views import APIView
from user.views.decorator import EnableDisableDecorator


class DeleteUser(APIView):
    @EnableDisableDecorator()
    def delete(self, request, userid):
        return {"is_deleted": True}

