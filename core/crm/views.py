from django.shortcuts import render
from .models import CarBuyerUsers, CallMeUsers, WaitingListUsers
from .serializers import CallMeSerializer, CarBuyerSerializer, WaitingListSerializer
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.generics import GenericAPIView
from rest_framework import mixins
from core.decorators import api_key

# Create your views here.

class CallMeAPI(GenericAPIView,mixins.ListModelMixin,mixins.UpdateModelMixin):
    serializer_class = CallMeSerializer
    queryset = CallMeUsers.objects.all()

    @api_key
    def get(self, request):
        return self.list(request)


class EditCallMeAPI(GenericAPIView,mixins.UpdateModelMixin):
    serializer_class = CallMeSerializer
    queryset = CallMeUsers.objects.all()
    lookup_field = 'pk'

    @api_key
    def put(self, request, pk):
        try:
            self.update(request,pk)
            return JsonResponse({"response":"Update has been successfully!"})
        except:
            return JsonResponse({"error":"Bele id-de mehsul tapilmadi"})
        


class CarBuyerAPI(GenericAPIView, mixins.ListModelMixin):
    serializer_class = CarBuyerSerializer
    queryset = CarBuyerUsers.objects.all()

    @api_key
    def get(self, request):
        return self.list(request)

class EditCarBuyerApi(GenericAPIView, mixins.UpdateModelMixin):
    serializer_class = CarBuyerSerializer
    queryset = CarBuyerUsers.objects.all()
    lookup_field = 'pk'

    @api_key
    def put(self, request, pk):
        try:
            self.update(request,pk)
            return JsonResponse({"response":"Update has been successfully!"})
        except:
            return JsonResponse({"error":"Bele id-de mehsul tapilmadi"})



class WaitingListAPI(GenericAPIView, mixins.ListModelMixin):
    serializer_class = WaitingListSerializer
    queryset = WaitingListUsers.objects.all()

    @api_key
    def get(self, request):
        return self.list(request)

class EditWaitingListAPI(GenericAPIView, mixins.UpdateModelMixin):
    serializer_class = WaitingListSerializer
    queryset = WaitingListUsers.objects.all()
    lookup_field = 'pk'

    @api_key
    def put(self, request, pk):
        try:
            self.update(request,pk)
            return JsonResponse({"response":"Update has been successfully!"})
        except:
            return JsonResponse({"error":"Bele id-de mehsul tapilmadi"})