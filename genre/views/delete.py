from rest_framework.views import APIView
from genre.views.decorator import EnableDisableDecorator
from rest_framework.permissions import IsAuthenticated
from core.permissions import IsStaff, IsSuperuser


class DeleteGenre(APIView):
    permission_classes = [IsAuthenticated & (IsStaff | IsSuperuser)]
    @EnableDisableDecorator()
    def delete(self, request, genreid):
       
        return {"is_deleted": True}