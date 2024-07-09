from django.urls import path
from user.views.login import Login
from user.views.credential import Credential
from user.views.get import GetUserSpecific, GetCSRF
from user.views.create import CreateUser
from user.views.edit import EditUser, EditStaff
from user.views.delete import DeleteUser, DeleteStaff
from user.views.recover import RecoverUser, RecoverStaff
from user.views.get import GetUser, GetDisabledArtist, GetDeletedUser
from user.views.get import GetArtist
from user.views.get import GetArtistSpecific
from user.views.get import GetStaffManage,GetDeletedStaffManage, GetDisabledStaffManage,GetStaffSpecific
from user.views.enable import EnableUser
from user.views.disable import DisableUser
from user.views.remove_profile import ProfileImageRemove
from user.views.remove_cover import CoverImageRemove
from user.views.get import GetLoggedInUser,CountryListView,ArtistCountView,UserCountView,CountryDataAPIView,UserCreationStats
from user.views.get import GetArtistManage, GetDeletedArtistManage, GetDisabledArtistManage, GetDeletedUserManage, GetDisabledUserManage, GetUserManage




urlpatterns = [

    
    path('getCSRF/', GetCSRF.as_view(), name="get_csrf"),
    
    path('user/get/', GetUser.as_view(), name="get_user"),
    path('user/get/deleted/', GetDeletedUser.as_view(), name="get_deleted_user"),



    path('user/get/manage/', GetUserManage.as_view(), name="get_user_manage"),
    path('user/get/deleted/manage/', GetDeletedUserManage.as_view(), name="get_deleted_user_manage"),
    path('user/get/disabled/manage/', GetDisabledUserManage.as_view(), name="get_disabled_user_manage"),


    path('artist/get/manage/', GetArtistManage.as_view(), name="get_artist_manage"),
    path('artist/get/deleted/manage/', GetDeletedArtistManage.as_view(), name="get_deleted_artist_manage"),
    path('artist/get/disabled/manage/', GetDisabledArtistManage.as_view(), name="get_disabled_artist_manage"),





    path('user/get/<int:userid>/', GetUserSpecific.as_view(), name="get_user_specific"),
    path('user/post/', CreateUser.as_view(), name="post_user"),
    path('user/edit/', EditUser.as_view(), name="edit_user"),
    path('user/delete/<int:userid>/', DeleteUser.as_view(), name="delete_user"),
    path('user/recover/<int:userid>/', RecoverUser.as_view(), name="recover_user"),

    path('staff/edit/<int:userid>/', EditStaff.as_view(), name="edit_staff"),
    path('staff/delete/<int:userid>/', DeleteStaff.as_view(), name="delete_staff"),
    path('staff/recover/<int:userid>/', RecoverStaff.as_view(), name="recover_staff"),

    path('login/', Login.as_view(),name='login'),
    path('credential/', Credential.as_view(),name='credential'),
    path('artist/get/', GetArtist.as_view(), name="get_artist"),
    path('staff/get/manage/', GetStaffManage.as_view(), name="get_staff"),
    path('staff/get/deleted/manage/', GetDeletedStaffManage.as_view(), name="get_deleted_staff"),
    path('staff/get/disabled/manage/', GetDisabledStaffManage.as_view(), name="get_disabled_staff"),
    path('artist/get/disabled/', GetDisabledArtist.as_view(), name="get_disabled_artist"),
    path('artist/get/<int:artistid>/', GetArtistSpecific.as_view(), name="get_artist_specific"),
    path('staff/get/<int:staffid>/', GetStaffSpecific.as_view(), name="get_staff_specific"),
    path('user/disable/<int:userid>/', DisableUser.as_view(), name="disable_user"),
    path('user/enable/<int:userid>/', EnableUser.as_view(), name="enable_user"),
    path('user/login-user/', GetLoggedInUser.as_view(), name='get_login_user_detail'),
    path('user/countrylistview/', CountryListView.as_view(), name='country_list_view'),
    path('user/artist-count/', ArtistCountView.as_view(), name='artist-count'),
    path('user/user-count/', UserCountView.as_view(), name='user-count'),
    path('country/country-data/', CountryDataAPIView.as_view(), name='country_data'),
    path('user/user-creation-stats/', UserCreationStats.as_view(), name='user_creation_stats'),
    path('users/profile-delete/<int:pk>/', ProfileImageRemove.as_view(), name='profile-image-delete'),
    path('users/cover-delete/<int:pk>/', CoverImageRemove.as_view(), name='cover-image-delete'),

]