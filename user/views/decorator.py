

from rest_framework.response import Response
from rest_framework import status
from user.models import Users
from user.serializers import UserSerializer

class EnableDisableDecorator:
    def __call__(self, func):
        def wrapper(instance, request, userid):
            try:
                user = Users.objects.get(id=userid)
            except Users.DoesNotExist:
                return Response({"msg": "User not found"}, status=status.HTTP_404_NOT_FOUND)
            if user != request.user and not request.user.is_staff and not request.user.is_superuser:
                return Response({"msg": "You do not have permission to perform this action."}, status=status.HTTP_403_FORBIDDEN)
            toggledata = func(instance, request, userid)
            serializer = UserSerializer(instance=user, data=toggledata, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return wrapper