from django.urls import path
from music.views.get import GetMusic, GetLike, GetComment
from music.views.get import GetMusicSpecific,GetAlbumMusicSpecific
from music.views.create import CreateMusic, CreateLike, CreateComment
from music.views.edit import EditMusic, EditComment
from music.views.delete import DeleteMusic, DeleteComment, DeleteLike
from music.views.recover import RecoverMusic
from music.views.enable import EnableMusic
from music.views.disable import DisableMusic
from music.views.hide import HideMusic
from music.views.unhide import UnHideMusic



urlpatterns = [
    path('music/get/', GetMusic.as_view(), name="get_music"),
    path('music/get/like/<int:musicid>/', GetLike.as_view(), name="get_like"),
    path('music/get/comment/<int:musicid>/', GetComment.as_view(), name="get_comment"),
    path('music/get/<int:musicid>/', GetMusicSpecific.as_view(), name="get_music_specific"),
    path('music/get/album/<int:albumid>/', GetAlbumMusicSpecific.as_view(), name="get_album_music_specific"),

    path('music/post/', CreateMusic.as_view(), name="post_music"),
    path('music/like/', CreateLike.as_view(), name="like_music"),
    path('music/comment/', CreateComment.as_view(), name="comment_music"),

    path('music/edit/<int:musicid>/', EditMusic.as_view(), name="edit_music"),
    path('music/edit/comment/<int:commentid>/', EditComment.as_view(), name="edit_comment"),

    path('music/disable/<int:musicid>/', DisableMusic.as_view(), name="disable_music"),
    path('music/enable/<int:musicid>/', EnableMusic.as_view(), name="enable_music"),

    path('music/hide/<int:musicid>/', HideMusic.as_view(), name="disable_music"),
    path('music/unhide/<int:musicid>/', UnHideMusic.as_view(), name="enable_music"),

    path('music/delete/<int:musicid>/', DeleteMusic.as_view(), name="delete_music"),
    path('music/recover/<int:musicid>/', RecoverMusic.as_view(), name="recover_music"),
    path('music/unlike/<int:likeid>/', DeleteLike.as_view(), name="delete_like"),
    path('music/delete/comment/<int:commentid>/', DeleteComment.as_view(), name="delete_comment"),
]