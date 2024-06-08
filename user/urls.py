from django.urls import path
from user.views.login import Login
from user.views.get import GetUserSpecific, GetCSRF
from user.views.create import CreateUser
from user.views.edit import EditUser
from user.views.delete import DeleteUser
from user.views.recover import RecoverUser
from user.views.get import GetUser, GetDeletedArtist, GetDeletedUser
from user.views.get import GetArtist
from user.views.get import GetArtistSpecific
from user.views.enable import EnableUser
from user.views.disable import DisableUser
from user.views.get import GetLoggedInUser




urlpatterns = [

    
    path('getCSRF/', GetCSRF.as_view(), name="get_csrf"),
    
    path('user/get/', GetUser.as_view(), name="get_user"),
    path('user/get/deleted/', GetDeletedUser.as_view(), name="get_deleted_user"),
    path('user/get/<int:userid>/', GetUserSpecific.as_view(), name="get_user_specific"),
    path('user/post/', CreateUser.as_view(), name="post_user"),
    path('user/edit/<int:userid>/', EditUser.as_view(), name="edit_user"),
    path('user/delete/<int:userid>/', DeleteUser.as_view(), name="delete_user"),
    path('user/recover/<int:userid>/', RecoverUser.as_view(), name="recover_user"),
    path('login/', Login.as_view(),name='login'),
    path('artist/get/', GetArtist.as_view(), name="get_artist"),
    path('artist/get/deleted/', GetDeletedArtist.as_view(), name="get_deleted_artist"),
    path('artist/get/<int:artistid>/', GetArtistSpecific.as_view(), name="get_artist_specific"),
    path('user/disable/<int:userid>/', DisableUser.as_view(), name="disable_user"),
    path('user/enable/<int:userid>/', EnableUser.as_view(), name="enable_user"),
    path('user/login-user/', GetLoggedInUser.as_view(), name='get_login_user_detail'),
]