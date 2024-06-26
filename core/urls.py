from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import include, path

from django.conf.urls import handler404
from .views import custom_404

handler404 = custom_404


from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView
)


urlpatterns = [
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('admin/', admin.site.urls),  
    path('api/', include('music.urls')),
    path('api/', include('user.urls')),
    path('api/', include('album.urls')),
    path('api/', include('genre.urls')),
    path('api/', include('band.urls')),
    path('api/', include('customizeable.urls')),

] + static(settings.MEDIA_URL,  document_root=settings.MEDIA_ROOT)
