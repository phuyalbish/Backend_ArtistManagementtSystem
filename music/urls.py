from django.urls import path

from music.views.get import GetMusic, GetComment, GetMusicSpecific,GetAlbumMusicSpecific, GetArtistSpecificMusic, GetLoggedInSpecificMusic, GetDeletedMusic, GetLoggedInSpecificDeletedMusic, GetMusicFromGenreWeather, GetMusicFromGenre, GetAllMusicWithGenre, MusicCountView,UserLikedMusicList,NewlyCreatedMusicView,GetAdminMusic
from music.views.create import CreateMusic, CreateComment, CreateCommentReply, ToggleMusicLike, ToggleCommentLike, ToggleCommentReplyLike

from music.views.edit import EditMusic, EditComment
from music.views.delete import DeleteMusic, DeleteComment, DeleteCommentReply
from music.views.recover import RecoverMusic
from music.views.enable import EnableMusic
from music.views.disable import DisableMusic
from music.views.hide import HideMusic
from music.views.unhide import UnHideMusic



urlpatterns = [
    path('music/get/', GetMusic.as_view(), name="get_music"),
    path('music/admin/get/', GetAdminMusic.as_view(), name="get_admin_music"),
    path('music/get/genre/<int:genreid>', GetMusicFromGenre.as_view(), name="get_music_specific_genre"),
    
    path('music/get/genre/', GetAllMusicWithGenre.as_view(), name="get_music_gemre"),

    path('music/get/weather/<str:weathername>', GetMusicFromGenreWeather.as_view(), name="get_music_from_weather"),

    
    path('music/get/loggedin/', GetLoggedInSpecificMusic.as_view(), name="get_music_loggedIn"),
    path('music/get/deleted/', GetDeletedMusic.as_view(), name="get_deleted_music"),
    path('music/get/loggedin/deleted/', GetLoggedInSpecificDeletedMusic.as_view(), name="get_music_loggedIn"),
    path('music/get/comment/<int:musicid>/', GetComment.as_view(), name="get_comment"),
    path('music/get/<int:musicid>/', GetMusicSpecific.as_view(), name="get_music_specific"),
    path('music/get/album/<int:albumid>/', GetAlbumMusicSpecific.as_view(), name="get_album_music_specific"),

    path('music/post/', CreateMusic.as_view(), name="post_music"),
    path('music/comment/', CreateComment.as_view(), name="comment_music"),
    path('music/comment/reply/', CreateCommentReply.as_view(), name="reply_comment"),

    path('music/likeunlike/<int:musicid>/', ToggleMusicLike.as_view(), name="toggle_like_music"),
    path('music/likeunlike/comment/<int:commentid>/', ToggleCommentLike.as_view(), name="toggle_like_music"),
    path('music/likeunlike/comment/reply/<int:commentid>/', ToggleCommentReplyLike.as_view(), name="toggle_like_music"),

    path('music/edit/<int:musicid>/', EditMusic.as_view(), name="edit_music"),
    path('music/edit/comment/<int:commentid>/', EditComment.as_view(), name="edit_comment"),

    path('music/disable/<int:musicid>/', DisableMusic.as_view(), name="disable_music"),
    path('music/enable/<int:musicid>/', EnableMusic.as_view(), name="enable_music"),

    path('music/hide/<int:musicid>/', HideMusic.as_view(), name="disable_music"),
    path('music/unhide/<int:musicid>/', UnHideMusic.as_view(), name="enable_music"),

    path('music/delete/<int:musicid>/', DeleteMusic.as_view(), name="delete_music"),
    path('music/recover/<int:musicid>/', RecoverMusic.as_view(), name="recover_music"),
    path('music/delete/comment/<int:commentid>/', DeleteComment.as_view(), name="delete_comment"),

    path('music/artist/get/<int:artistid>/', GetArtistSpecificMusic.as_view(), name="get_artist_music"),
     path('music/music-count/', MusicCountView.as_view(), name='music-count'),

    path('music/delete/comment/reply/<int:commentid>/', DeleteCommentReply.as_view(), name="delete_comment_reply"),
    path('music/artist/get/<int:artistid>/', GetArtistSpecificMusic.as_view(), name="get_artist_music"),
    path('user/liked/', UserLikedMusicList.as_view(), name='user-liked-music'),
    # path('liked/album/', UserLikedAlbumList.as_view(), name='user-liked-album-list'),
    path('user/newly-joined-music/', NewlyCreatedMusicView.as_view(), name='newly-joined-artists'),

]