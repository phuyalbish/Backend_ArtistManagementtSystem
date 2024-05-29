from django.urls import path
from user.views.get import GetUser


urlpatterns = [
    path('/user/get', GetUser.as_view(), name="get_user")
]