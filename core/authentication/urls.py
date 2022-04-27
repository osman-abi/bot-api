from django.urls import path
from .views import UserAuthAPI

urlpatterns = [
    path('users/', UserAuthAPI.as_view())
]