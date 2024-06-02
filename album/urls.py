from django.urls import path
from album.views.get import GetAlbum
from album.views.get import GetAlbumSpecific
from album.views.create import CreateAlbum
from album.views.edit import EditAlbum
from album.views.delete import DeleteAlbum
from album.views.recover import RecoverAlbum
from album.views.enable import EnableAlbum
from album.views.disable import DisableAlbum


urlpatterns = [
    path('album/get/', GetAlbum.as_view(), name="get_album"),
    path('album/get/<int:albumid>/', GetAlbumSpecific.as_view(), name="get_album_specific"),
    path('album/post/', CreateAlbum.as_view(), name="post_album"),
    path('album/edit/<int:albumid>/', EditAlbum.as_view(), name="edit_album"),
    path('album/delete/<int:albumid>/', DeleteAlbum.as_view(), name="delete_album"),
    path('album/recover/<int:albumid>/', RecoverAlbum.as_view(), name="recover_album"),
    path('album/disable/<int:albumid>/', DisableAlbum.as_view(), name="disable_album"),
    path('album/enable/<int:albumid>/', EnableAlbum.as_view(), name="enable_album"),
]