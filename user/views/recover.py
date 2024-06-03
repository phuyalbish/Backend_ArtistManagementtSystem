from rest_framework.views import APIView
from user.views.decorator import EnableDisableDecorator
from core.permissions import IsNormalUser, IsArtist,IsBand
from rest_framework.permissions import IsAuthenticated
from user.models import Users
from rest_framework.exceptions import PermissionDenied


class RecoverUser(APIView):
    permission_classes = [IsAuthenticated,  IsNormalUser | IsArtist | IsBand]
    @EnableDisableDecorator()
    def delete(self, request, userid):
        user = Users.objects.get(id=userid)
        if request.user.id != user.id:
            raise PermissionDenied("You do not have permission to perform this action.")
        return {"is_deleted": False}
