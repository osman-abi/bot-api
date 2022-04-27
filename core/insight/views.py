from unicodedata import name
from django.shortcuts import render
from rest_framework.views import APIView
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.generics import GenericAPIView
from rest_framework import mixins
from contact.models import Contacts
from core.decorators import api_key

# Create your views here.


class InsightAPI(APIView):
    
    @api_key
    def get(self, request):
        users_count = Contacts.objects.count()
        male_percent = (Contacts.objects.filter(gender='male').count() / users_count)*100
        female_percent = 100 - male_percent

        return JsonResponse({
            'users_count':users_count,
            'male_percent':male_percent,
            'female_percent':female_percent
        })


class FilterUserStatistics(APIView):
    
    pass