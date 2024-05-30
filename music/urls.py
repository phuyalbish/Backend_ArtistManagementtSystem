from django.urls import path
from music.views.get import GetMusic
from music.views.get import GetMusicSpecific
from music.views.create import CreateMusic
from music.views.edit import EditMusic
from music.views.delete import DeleteMusic
from music.views.recover import RecoverMusic


urlpatterns = [
    path('music/get/', GetMusic.as_view(), name="get_music"),
    path('music/get/<int:musicid>/', GetMusicSpecific.as_view(), name="get_music_specific"),
    path('music/post/', CreateMusic.as_view(), name="post_music"),
    path('music/edit/<int:musicid>/', EditMusic.as_view(), name="edit_music"),
    path('music/delete/<int:musicid>/', DeleteMusic.as_view(), name="delete_music"),
    path('music/recover/<int:musicid>/', RecoverMusic.as_view(), name="recover_music"),
]