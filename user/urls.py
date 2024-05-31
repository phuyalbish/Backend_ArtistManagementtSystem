from django.urls import path
from .views.login import Login
from user.views.get import GetUserSpecific
from user.views.create import CreateUser
from user.views.edit import EditUser
from user.views.delete import DeleteUser
from user.views.recover import RecoverUser
from user.views.get import GetUser
from user.views.get import GetArtist
from user.views.get import GetArtistSpecific
from user.views.create import CreateArtist
from user.views.edit import EditArtist




urlpatterns = [
    path('user/get/', GetUser.as_view(), name="get_user"),
    path('user/get/<int:userid>/', GetUserSpecific.as_view(), name="get_user_specific"),
    path('user/post/', CreateUser.as_view(), name="post_user"),
    path('user/edit/<int:userid>/', EditUser.as_view(), name="edit_user"),
    path('user/delete/<int:userid>/', DeleteUser.as_view(), name="delete_user"),
    path('user/recover/<int:userid>/', RecoverUser.as_view(), name="recover_user"),
    path('login/', Login.as_view(),name='login'),
    path('artist/get/', GetArtist.as_view(), name="get_artist"),
    path('artist/get/<int:artistid>/', GetArtistSpecific.as_view(), name="get_artist_specific"),
    path('artist/post/', CreateArtist.as_view(), name="post_artist"),
    path('artist/edit/<int:artistid>/', EditArtist.as_view(), name="edit_artist"),
]