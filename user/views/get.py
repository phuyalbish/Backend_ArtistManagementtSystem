
from rest_framework import generics, filters
import django
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from user.serializers import UserSerializer
from user.models import Users
from rest_framework.permissions import AllowAny, IsAuthenticated
from django.db.models import Count
from django.db.models.functions import TruncDate
from core.permissions import  IsStaff, IsSuperuser
from core.views import StandardPagination


class GetArtistManage(generics.ListAPIView):
    permission_classes = [IsStaff]
    serializer_class = UserSerializer
    pagination_class = StandardPagination
    filter_backends = (filters.SearchFilter,)
    search_fields = ('username','firstname', 'lastname','email','gender',)

    def get_queryset(self):
        return Users.objects.filter(is_deleted=False, is_artist=True, is_staff=False)
    

class GetDisabledArtistManage(generics.ListAPIView):
    permission_classes = [IsStaff]
    serializer_class = UserSerializer
    pagination_class = StandardPagination
    filter_backends = (filters.SearchFilter,)
    search_fields = ('username','firstname', 'lastname','email','gender',)

    def get_queryset(self):
        return Users.objects.filter(is_deleted=False, is_disabled=True, is_artist=True,is_staff=False)
    

class GetDeletedArtistManage(generics.ListAPIView):
    permission_classes = [IsStaff]
    serializer_class = UserSerializer
    pagination_class = StandardPagination
    filter_backends = (filters.SearchFilter,)
    search_fields = ('username','firstname', 'lastname','email','gender',)
    def get_queryset(self):
        return Users.objects.filter(is_deleted=True, is_artist=True, is_staff=False)
    



class GetUserManage(generics.ListAPIView):
    permission_classes = [IsStaff]
    serializer_class = UserSerializer
    pagination_class = StandardPagination
    filter_backends = (filters.SearchFilter,)
    search_fields = ('username','firstname', 'lastname','email','gender',)
    def get_queryset(self):
        return Users.objects.filter(is_deleted=False, is_artist=False, is_staff=False)
    

class GetDisabledUserManage(generics.ListAPIView):
    permission_classes = [IsStaff]
    serializer_class = UserSerializer
    pagination_class = StandardPagination
    filter_backends = (filters.SearchFilter,)
    search_fields = ('username','firstname', 'lastname','email','gender',)
    def get_queryset(self):
        return Users.objects.filter(is_deleted=False, is_disabled=True, is_artist=False, is_staff=False)
    

class GetDeletedUserManage(generics.ListAPIView):
    permission_classes = [IsStaff]
    serializer_class = UserSerializer
    pagination_class = StandardPagination
    filter_backends = (filters.SearchFilter,)
    search_fields = ('username','firstname', 'lastname','email','gender',)
    def get_queryset(self):
        return Users.objects.filter(is_deleted=True, is_artist=False, is_staff=False)



class GetStaffManage(generics.ListAPIView):
    permission_classes = [IsSuperuser]
    serializer_class = UserSerializer
    pagination_class = StandardPagination
    filter_backends = (filters.SearchFilter,)
    search_fields = ('username','firstname', 'lastname','email','gender',)
    def get_queryset(self):
        return Users.objects.filter(is_deleted=False, is_staff=True, is_superuser=False)
    

class GetDeletedStaffManage(generics.ListAPIView):
    permission_classes = [IsSuperuser]
    serializer_class = UserSerializer
    pagination_class = StandardPagination
    filter_backends = (filters.SearchFilter,)
    search_fields = ('username','firstname', 'lastname','email','gender',)
    def get_queryset(self):
        return Users.objects.filter(is_deleted=True, is_staff=True, is_superuser=False)


class GetDisabledStaffManage(generics.ListAPIView):
    permission_classes = [IsSuperuser]
    serializer_class = UserSerializer
    pagination_class = StandardPagination
    filter_backends = (filters.SearchFilter,)
    search_fields = ('username','firstname', 'lastname','email','gender',)
    def get_queryset(self):
        return Users.objects.filter(is_deleted=False, is_disabled=True, is_staff=True, is_superuser=False)
    






class GetUser(APIView):
    permission_classes = [AllowAny]
    def get(self, request):
        try:
            datas = Users.objects.filter(is_deleted=False, is_artist=False, is_superuser=False)
            serializer = UserSerializer(datas, many=True)
        except:
            return Response({"detail":"No User Found"}, status=404)
        return Response(serializer.data)



class GetArtist(APIView):
    permission_classes = [AllowAny]
    def get(self, request):
        try:
            datas = Users.objects.filter(is_deleted=False, is_artist=True, is_superuser=False)
            artist_serializer = UserSerializer(datas, many=True)
        except:
            return Response({"detail":"No Artist Found"}, status=404)
        return Response(artist_serializer.data, status=status.HTTP_200_OK)





class GetUserSpecific(APIView):
    permission_classes = [AllowAny]
    def get(self, request, userid):
        try:
            data = Users.objects.get(pk=userid, is_deleted=False)
            serializer = UserSerializer(data, many=False)
        except:
            return Response({"detail":"No User Found"}, status=404)
        return Response(serializer.data)

class GetArtistSpecific(APIView):
    permission_classes = [AllowAny]
    def get(self, request, artistid):
        try:
            data = Users.objects.get(pk=artistid, is_artist=True, is_deleted=False)
            serializer = UserSerializer(data, many=False)
        except:
            return Response({"detail":"No Artist Found"}, status=404)
        return Response(serializer.data)
    
class GetStaffSpecific(APIView):
    permission_classes = [AllowAny]
    def get(self, request, staffid):
        try:
            data = Users.objects.get(pk=staffid, is_staff=True, is_deleted=False)
            serializer = UserSerializer(data, many=False)
            return Response(serializer.data)
        except:
            return Response({"detail":"No Staff Found"}, status=404)



        
    

class GetLoggedInUser(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        serializer = UserSerializer(user)
        return Response(serializer.data)


class CountryListView(APIView):
    def get(self, request, *args, **kwargs):
        countries = [country[0] for country in Users.ASIAN_COUNTRIES]
        return Response({'countries': countries})

class ArtistCountView(APIView):
    def get(self, request, *args, **kwargs):
        total_artists = Users.objects.filter(is_artist=True).count()
        return Response({'total_artists': total_artists})

class UserCountView(APIView):
    def get(self, request, *args, **kwargs):
        total_users = Users.objects.count()
        return Response({'total_users': total_users})



class CountryDataAPIView(APIView):
    def get(self, request):
        
        country_data = Users.objects.values('country').annotate(count=Count('id'))

        
        formatted_data = [{'country': item['country'], 'count': item['count']} for item in country_data]

        return Response(formatted_data, status=status.HTTP_200_OK)


class UserCreationStats(APIView):
    def get(self, request, *args, **kwargs):
        data = Users.objects.annotate(date=TruncDate('created_at')).values('date').annotate(count=Count('id')).order_by('date')

        response_data = {
            'dates': [entry['date'] for entry in data],
            'counts': [entry['count'] for entry in data]
        }

        return Response(response_data)

    

class GetCSRF(APIView):
    permission_classes = [AllowAny]
    def getCSRFToken(request):
        try:
            token = django.middleware.csrf.get_token(request)
        except:
            return Response({'detail':"Token Not Found"}, status=404)
        return Response({'token': token})




class GetDeletedUser(APIView):
    permission_classes = [AllowAny]
    def get(self, request):
        try:
            datas = Users.objects.filter(is_deleted=True,  is_artist=False, is_superuser=False)
            serializer = UserSerializer(datas, many=True)
        except:
            return Response({"detail":"No User Found"}, status=404)
        return Response(serializer.data)



class GetDisabledArtist(APIView):
    permission_classes = [AllowAny]
    def get(self, request):
        try:
            datas = Users.objects.filter(is_disabled=True, is_artist=True, is_superuser=False)
            artist_serializer = UserSerializer(datas, many=True)
        except:
            return Response({"detail":"No Artist Found"}, status=404)
        return Response(artist_serializer.data, status=status.HTTP_200_OK)
    


