from django.urls import path
from .views.logout import Login

urlpatterns = [
    path('login/', Login.as_view(),name='login'),
]