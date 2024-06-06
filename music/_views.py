# import django
# from .models import Music
# from django.views.decorators.csrf import csrf_exempt
# from .serializers import MusicSerializer
# from rest_framework.decorators import api_view, permission_classes
# from rest_framework.permissions import IsAuthenticated
# from rest_framework.response import Response
# from rest_framework import status


# def enable_disable(func):
#     def wrapper(request, musicid):
#         try:
#             user = Music.objects.get(id=musicid)
#         except Music.DoesNotExist:
#             return Response({"msg": "Music not found"}, status=status.HTTP_404_NOT_FOUND)
#         toggledata = func(request, musicid)
#         serializer = MusicSerializer(instance=user, data=toggledata, partial=True)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_200_OK)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#     return wrapper


# @api_view(['GET'])
# @permission_classes([IsAuthenticated])
# def get(request):
#     try:
#         datas = list(Music.objects.filter(is_deleted=False))
#         serializer = MusicSerializer(datas, many=True)
#     except:
#         return Response({"detail":"No Music Found"}, status=404)
#     return Response(serializer.data)
    


# @api_view(['GET'])
# @permission_classes([IsAuthenticated])
# def getUser(request,musicid):
#     try:
#         data = Music.objects.get(pk=musicid, is_deleted=False)
#         serializer = MusicSerializer(data, many=False)
#     except:
#         return Response({"detail":"No Music Found"}, status=404)
#     return Response(serializer.data)




# @api_view(['POST'])
# @permission_classes([IsAuthenticated])
# @isArtist
# def add(request):
    
#     serializer = MusicSerializer(data=request.data)
#     if serializer.is_valid():
#         serializer.save()
#         return Response(serializer.data)
#     else:
#         return Response(serializer.errors, status=422)
    


# @permission_classes([IsAuthenticated])
# @api_view(['PATCH'])
# @isArtist
# def edit(request,musicid):
#     try:
#         user = Music.objects.get(id=musicid)
#     except Music.DoesNotExist:
#         return Response({"msg": "Music not found"}, status=status.HTTP_404_NOT_FOUND)
#     serializer = MusicSerializer(instance=user, data=request.data, partial=True)
#     if serializer.is_valid():
#         serializer.save()
#         return Response(serializer.data, status=status.HTTP_200_OK)
#     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# @api_view(['PATCH'])
# @permission_classes([IsAuthenticated])
# @isArtist
# @enable_disable
# def delete(request,musicid):
#     return {"is_deleted": True}


# @api_view(['PATCH'])
# @permission_classes([IsAuthenticated])
# @isArtist
# @enable_disable
# def restore(request,musicid):
#     return {"is_deleted": False}


# @api_view(['PATCH'])
# @permission_classes([IsAuthenticated])
# @isArtist
# @enable_disable
# def hide_music(request,musicid):
#     return {"is_hidden": True}

# @csrf_exempt
# @api_view(['PATCH'])
# @isArtist
# @enable_disable
# def show_music(request,musicid):
#     return {"is_hidden": False}



# @api_view(['PATCH'])
# @permission_classes([IsAuthenticated])
# @isStaff
# @enable_disable
# def disable_music(request, musicid):
#     return {"is_disabled": True}



# @api_view(['PATCH'])
# @permission_classes([IsAuthenticated])
# @isStaff
# @enable_disable
# def enable_music(request, musicid):
#     return {"is_disabled": False}






# @api_view(['GET'])
# @permission_classes([IsAuthenticated])
# def getUserSpecificMusic(request, userid):
#     try:
#         datas = Music.objects.filter(artist=userid, is_deleted=False)
#         # user = User.get(pk=request.user_id)
#         # user.album.all()
#         serializer = MusicSerializer(datas, many=True)
#     except:
#         return Response({"detail":"No Album Found"}, status=404)
#     return Response(serializer.data)
    
