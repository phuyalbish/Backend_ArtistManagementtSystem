from rest_framework.response import Response
from rest_framework import status
from customizeable.models import CustomTheme, CustomThemeSerializer

class EnableDisableDecorator:
    def __call__(self, func):
        def wrapper(instance, request, themeid):
            try:
                theme = CustomTheme.objects.get(id=themeid)
            except CustomTheme.DoesNotExist:
                return Response({"msg": "Theme not found"}, status=status.HTTP_404_NOT_FOUND)
            toggledata = func(instance, request, themeid)
            serializer = CustomThemeSerializer(instance=theme, data=toggledata, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return wrapper