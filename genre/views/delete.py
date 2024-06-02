from rest_framework.views import APIView
from genre.views.decorator import EnableDisableDecorator


class DeleteGenre(APIView):
    @EnableDisableDecorator()
    def delete(self, request, genreid):
       
        return {"is_deleted": True}