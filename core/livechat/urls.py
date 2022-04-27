from django.urls import path
from .views import FacebookBotView

urlpatterns = [

    path('webhooks/facebook/webhook', FacebookBotView.as_view())
]