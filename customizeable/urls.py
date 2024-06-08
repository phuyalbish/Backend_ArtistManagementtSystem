from customizeable.views import SelectTheme
from django.urls import path

urlpatterns = [
    path('user/setCustomTheme/', SelectTheme.as_view(), name="setCustomTheme"),

]