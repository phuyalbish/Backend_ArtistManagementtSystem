from customizeable._views import SelectTheme, UnSelectTheme
from customizeable.views.get import GetTheme, GetDeletedTheme, GetSpecificTheme
from customizeable.views.create import CreateTheme
from customizeable.views.edit import EditTheme
from customizeable.views.delete import DeleteTheme
from customizeable.views.recover import RecoverTheme
from django.urls import path

urlpatterns = [
    path('user/theme/set/<int:themeid>/', SelectTheme.as_view(), name="setCustomTheme"),
    path('user/theme/unset/', UnSelectTheme.as_view(), name="unsetCustomTheme"),
    path('theme/get/', GetTheme.as_view(), name="get_theme"),
    path('theme/get/<int:themeid>/', GetSpecificTheme.as_view(), name="get_theme_specific"),
    path('theme/get/deleted/', GetDeletedTheme.as_view(), name="get_deleted_theme"),
    path('theme/create/', CreateTheme.as_view(), name="get_theme"),
    path('theme/edit/<int:themeid>/', EditTheme.as_view(), name="edit_theme"),
    path('theme/delete/<int:themeid>/', DeleteTheme.as_view(), name="delete_theme"),
    path('theme/recover/<int:themeid>/', RecoverTheme.as_view(), name="delete_theme")

]