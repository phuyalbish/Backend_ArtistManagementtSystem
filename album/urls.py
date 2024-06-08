from django.urls import path
from album.views.get import GetAlbum, GetComment, GetLoggedInSpecificAlbum, GetDeletedAlbum, GetLoggedInSpecificDeletedAlbum
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
    path('album/get/loggedin/', GetLoggedInSpecificAlbum.as_view()), 
    path('album/get/<int:albumid>/', GetAlbumSpecific.as_view(), name="get_album_specific"),
    path('album/get/deleted/', GetDeletedAlbum.as_view(), name="get_deleted_music"),
    path('album/get/loggedin/deleted/', GetLoggedInSpecificDeletedAlbum.as_view(), name="get_music_loggedIn"),


    path('album/post/', CreateAlbum.as_view(), name="post_album"),
    path('album/comment/', CreateComment.as_view(), name="comment_album"),
    path('album/comment/reply/', CreateCommentReply.as_view(), name="reply_comment"),

    path('album/edit/<int:albumid>/', EditAlbum.as_view(), name="edit_album"),
    path('album/delete/<int:albumid>/', DeleteAlbum.as_view(), name="delete_album"),
    path('album/recover/<int:albumid>/', RecoverAlbum.as_view(), name="recover_album"),
    path('album/disable/<int:albumid>/', DisableAlbum.as_view(), name="disable_album"),
    path('album/enable/<int:albumid>/', EnableAlbum.as_view(), name="enable_album"),

    path('album/hide/<int:albumid>/', HideAlbum.as_view(), name="disable_album"),
    path('album/unhide/<int:albumid>/', UnHideAlbum.as_view(), name="enable_album"),

    path('album/get/comment/<int:albumid>/', GetComment.as_view(), name="get_comment"),

    path('album/likeunlike/<int:albumid>/', ToggleAlbumLike.as_view(), name="toggle_like_album"),
    path('album/likeunlike/comment/<int:commentid>/', ToggleCommentLike.as_view(), name="toggle_like_album"),
    path('album/likeunlike/comment/reply/<int:commentid>/', ToggleCommentReplyLike.as_view(), name="toggle_like_album"),

]