from django.urls import path

from album.views.get import GetAlbum, GetComment, GetLoggedInSpecificAlbum, GetDeletedAlbum,GetDisabledAlbum,GetHiddenAlbum,  AlbumCountView,GetArtistSpecificAlbum
from album.views.get import GetAlbumManage, GetDeletedAlbumManage, GetDisabledAlbumManage, GetLoggedInSpecificAlbumManage, GetHiddenAlbumManage
from album.views.get import GetAlbumSpecific
from album.views.create import CreateAlbum, ToggleCommentLike, ToggleAlbumLike, ToggleCommentReplyLike, CreateComment, CreateCommentReply
from album.views.edit import EditAlbum
from album.views.delete import DeleteAlbum
from album.views.recover import RecoverAlbum
from album.views.enable import EnableAlbum
from album.views.disable import DisableAlbum
from album.views.hide import HideAlbum
from album.views.unhide import UnHideAlbum

urlpatterns = [
    path('album/get/', GetAlbum.as_view(), name="get_album"),
    path('album/get/loggedin/', GetLoggedInSpecificAlbum.as_view(), name="get_LoggedIn_specific_album_manage"), 
    path('album/get/<int:albumid>/', GetAlbumSpecific.as_view(), name="get_album_specific"),
    path('album/get/deleted/', GetDeletedAlbum.as_view(), name="get_deleted_album"),
    path('album/get/disabled/', GetDisabledAlbum.as_view(), name="get_disabled_album"),
    path('album/get/hidden/', GetHiddenAlbum.as_view(), name="get_hidden_album"),


    path('album/get/manage/', GetAlbumManage.as_view(), name="get_album_manage"),
    path('album/get/loggedin/manage/', GetLoggedInSpecificAlbumManage.as_view() , name="get_LoggedIn_specific_album_manage"), 
    path('album/get/deleted/manage/', GetDeletedAlbumManage.as_view(), name="get_deleted_album_manage"),
    path('album/get/disabled/manage/', GetDisabledAlbumManage.as_view(), name="get_disabled_album_manage"),
    path('album/get/hidden/manage/', GetHiddenAlbumManage.as_view(), name="get_hidden_album_manage"),

    path('album/post/', CreateAlbum.as_view(), name="post_album"),
    path('album/comment/', CreateComment.as_view(), name="comment_album"),
    path('album/comment/reply/', CreateCommentReply.as_view(), name="reply_comment"),
    path('album/edit/<int:albumid>/', EditAlbum.as_view(), name="edit_album"),
    path('album/delete/<int:albumid>/', DeleteAlbum.as_view(), name="delete_album"),
    path('album/recover/<int:albumid>/', RecoverAlbum.as_view(), name="recover_album"),
    path('album/disable/<int:albumid>/', DisableAlbum.as_view(), name="disable_album"),

    path('album/enable/<int:albumid>/', EnableAlbum.as_view(), name="enable_album"),

    path('album/album-count/', AlbumCountView.as_view(), name='album-count'),

    path('album/hide/<int:albumid>/', HideAlbum.as_view(), name="disable_album"),
    path('album/unhide/<int:albumid>/', UnHideAlbum.as_view(), name="enable_album"),

    path('album/get/comment/<int:albumid>/', GetComment.as_view(), name="get_comment"),

    path('album/likeunlike/<int:albumid>/', ToggleAlbumLike.as_view(), name="toggle_like_album"),
    path('album/likeunlike/comment/<int:commentid>/', ToggleCommentLike.as_view(), name="toggle_like_album"),
    path('album/likeunlike/comment/reply/<int:commentid>/', ToggleCommentReplyLike.as_view(), name="toggle_like_album"),
    path('album/artist/get/<int:artistid>/', GetArtistSpecificAlbum.as_view(), name="get_artist_music"),
]
