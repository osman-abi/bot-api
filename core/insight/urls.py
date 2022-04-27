from .views import InsightAPI
from django.urls import path

urlpatterns = [
    path('user-statistics/', InsightAPI.as_view())
]