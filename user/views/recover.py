from rest_framework.views import APIView
from user.views.decorator import EnableDisableDecorator
from core.permissions import IsNormalUser, IsArtist,IsBand, IsSuperuser
from rest_framework.permissions import IsAuthenticated
from user.models import Users


class RecoverUser(APIView):
    permission_classes = [IsAuthenticated,  IsNormalUser | IsArtist | IsBand | IsSuperuser]
    @EnableDisableDecorator()
    def delete(self, request, userid):
        user = Users.objects.get(id=userid)
        return {"is_deleted": False}



class RecoverStaff(APIView):
    permission_classes = [IsAuthenticated, IsSuperuser]
    @EnableDisableDecorator()
    def delete(self, request, userid):
        user = Users.objects.get(id=userid)
        return {"is_deleted": False}