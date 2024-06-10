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
from user.views.get import GetStaff,GetDeletedStaff,GetStaffSpecific
from user.views.enable import EnableUser
from user.views.disable import DisableUser
from user.views.get import GetLoggedInUser,CountryListView,ArtistCountView,UserCountView,CountryDataAPIView,UserCreationStats




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
    path('staff/get/', GetStaff.as_view(), name="get_staff"),
    path('artist/get/deleted/', GetDeletedArtist.as_view(), name="get_deleted_artist"),
    path('staff/get/deleted/', GetDeletedStaff.as_view(), name="get_deleted_staff"),
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

]