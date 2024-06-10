from django.urls import path
from genre.views.get import GetGenre, GetWeatherListView, GetGenreWithWeather
from genre.views.get import GetGenreSpecific
from genre.views.create import CreateGenre
from genre.views.edit import EditGenre
from genre.views.delete import DeleteGenre
from genre.views.recover import RecoverGenre

urlpatterns = [
    path('genre/get/weather/<str:weathername>/', GetGenreWithWeather.as_view(), name='get_genre_with_weather'),
    path('genre/get/weather/', GetWeatherListView.as_view(), name='weather_list_view'),
    path('genre/get/', GetGenre.as_view(), name="get_genre"),
    path('genre/get/<int:genreid>/', GetGenreSpecific.as_view(), name="get_genre_specific"),
    path('genre/post/', CreateGenre.as_view(), name="post_genre"),
    path('genre/edit/<int:genreid>/', EditGenre.as_view(), name="edit_genre"),
    path('genre/delete/<int:genreid>/', DeleteGenre.as_view(), name="delete_genre"),
    path('genre/recover/<int:genreid>/', RecoverGenre.as_view(), name="recover_genre"),
]