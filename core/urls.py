"""
URL configuration for core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls import handler404
from django.conf.urls.static import static
from django.contrib import admin
from django.shortcuts import render
from django.urls import include, path, re_path
from django.views.static import serve as static_serve
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)

handler404 = "core.views.custom_404"


def custom_404(request, _):
    return render(request, "404.html", status=404)


urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/token/verify/", TokenVerifyView.as_view(), name="token_verify"),
    path("api/token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("api/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path('api/', include('music.urls')),
    path('api/', include('user.urls')),
    path('api/', include('album.urls')),
    path('api/', include('genre.urls')),
    path('api/', include('band.urls')),
    path('api/', include('customizeable.urls')),
]

if settings.DEBUG:

    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


if not settings.DEBUG:
    urlpatterns += [
        re_path(
            r"^media/(?P<path>.*)$",
            static_serve,
            {
                "document_root": settings.MEDIA_ROOT,
            },
        ),
    ]
