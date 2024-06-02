from rest_framework.views import APIView
from user.views.decorator import EnableDisableDecorator
from core.permissions import IsOwner, IsStaff, IsSuperuser
from rest_framework.permissions import IsAuthenticated



class DeleteUser(APIView):
    permission_classes = [IsAuthenticated]
    @EnableDisableDecorator()
    def delete(self, request, userid):
        return {"is_deleted": True}

