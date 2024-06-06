from rest_framework.views import APIView
from album.views.decorator import EnableDisableDecorator
from rest_framework.permissions import IsAuthenticated
from core.permissions import IsStaff, IsSuperuser


class EnableAlbum(APIView):
    permission_classes = [IsAuthenticated & (IsStaff | IsSuperuser)]
    @EnableDisableDecorator()
    def delete(self, request, albumid):
       
        return {
            "modified_by" :request.user.id ,
            "is_disabled": False
        }