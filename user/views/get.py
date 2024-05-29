from rest_framework import status
from rest_framework.views import APIView



class GetUser(APIView):
    def get():
        print("Get")