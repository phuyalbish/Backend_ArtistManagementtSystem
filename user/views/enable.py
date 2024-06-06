from rest_framework.views import APIView
from user.views.decorator import EnableDisableDecorator
from core.permissions import IsSuperuser,IsStaff
from rest_framework.permissions import IsAuthenticated
from user.models import Users
from rest_framework.exceptions import PermissionDenied


class EnableUser(APIView):
    permission_classes = [IsAuthenticated,  IsStaff | IsSuperuser]
    @EnableDisableDecorator()
    def delete(self, request, userid):
        user = Users.objects.get(id=userid)
        if request.user.is_staff and user.is_superuser:
            raise PermissionDenied("You do not have permission to perform this action.")
        return {"is_disabled": False}