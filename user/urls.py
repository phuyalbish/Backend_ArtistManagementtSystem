from django.urls import path
from ._views import Login

urlpatterns = [
    path('login/', Login.as_view()),
]