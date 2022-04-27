from django.urls import path
from .views import CallMeAPI, EditCallMeAPI, CarBuyerAPI, EditCarBuyerApi, WaitingListAPI, EditWaitingListAPI


urlpatterns = [
    path('call-me-users/', CallMeAPI.as_view()),
    path('call-me-users/<int:pk>/', EditCallMeAPI.as_view()),

    path('car-buyer-users/', CarBuyerAPI.as_view()),
    path('car-buyer-users/<int:pk>/', EditCarBuyerApi.as_view()),

    path('waiting-list-users/', WaitingListAPI.as_view()),
    path('waiting-list-users/<int:pk>/', EditWaitingListAPI.as_view()),
]