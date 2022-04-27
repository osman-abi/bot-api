from django.shortcuts import render
from .models import Contacts, ReplyMessage
from .serializers import ContactSerializer, ReplyMessageSerializer
from rest_framework.views import APIView
from django.http import JsonResponse
from core.decorators import api_key
from rest_framework.response import Response
from rest_framework.generics import GenericAPIView
from rest_framework import mixins

import requests

# Access Token

ACCESS_TOKEN = 'EAAIyUoMs63QBAGnZC5Y8iUZA5E6ou2fhCbn5teJ4AdHBSZCwZCTllpDgJDuiZBDDlnuPDvpTrLLjqQZAAGlyTiqK4s0tj8o99wFATY4f3CQKwSTEWYLX9NjQXCuYNcvZBrXpIHU0TMxpmJg0TRRH02TadrWROwvsb9dxkVKdstLash6bcypWuwwpGOZCQXco6r4ZD'
PAGE_ID = 110270018314670


class ContactAPI(GenericAPIView, mixins.ListModelMixin):
    serializer_class = ContactSerializer
    queryset = Contacts.objects.all()

    @api_key
    def get(self,request):
        return self.list(request)

class DetailContactAPI(GenericAPIView, mixins.RetrieveModelMixin):
    serializer_class = ContactSerializer
    queryset = Contacts.objects.all()
    lookup_field = 'pk'

    def get(self, request, pk):
        return self.retrieve(request, pk)


class PostListAPI(APIView):

    @api_key
    def get(self,request):
        posts_url = 'https://graph.facebook.com/v13.0/{}/posts?access_token={}'.format(PAGE_ID, ACCESS_TOKEN)
        posts = requests.get(posts_url)
        return JsonResponse(posts.json())


class PostDetailAPI(APIView):

    @api_key
    def get(self,request,post_id):
        post_url = 'https://graph.facebook.com/v13.0/{}/comments?access_token={}'.format(post_id, ACCESS_TOKEN)
        post = requests.get(post_url)
        return JsonResponse(post.json())



class SendMessageCommentAuthor(APIView):

    @api_key
    def post(self,request,comment_id):
        headers = {'content-type': 'application/json'}
        body = {
            "messaging_type":"MESSAGE_TAG",
            "tag":"CONFIRMED_EVENT_UPDATE",
            "recipient": {
                "comment_id": comment_id
            },
            "message": {
                "text": "baklava nah sana baklava"
            }
        }
        url = 'https://graph.facebook.com/v13.0/me/messages?access_token={}'.format(ACCESS_TOKEN)

        r = requests.post(url, json=body, headers=headers)

        return JsonResponse(r.json())


class ReplyMessageAPI(GenericAPIView, mixins.ListModelMixin):
    serializer_class = ReplyMessageSerializer
    queryset = ReplyMessage.objects.all()

    @api_key
    def get(self, request):
        return self.list(request)


class ReplyMessageEditAPI(GenericAPIView, mixins.UpdateModelMixin):
    serializer_class = ReplyMessageSerializer
    queryset = ReplyMessage.objects.all()
    lookup_field = 'pk'

    @api_key
    def put(self, request, pk):
        try:
            self.update(request,pk)
            return JsonResponse({"response":"Update has been successfully!"})
        except:
            return JsonResponse({"error":"Bele id-de mehsul tapilmadi"})


# class WaitingListAPI(GenericAPIView, mixins.ListModelMixin):
#     serializer_class = WaitingListSerializer
#     queryset = WaitingListUsers.objects.all()

#     def get(self, request):
#         return self.list(request)

# class EditWaitingListAPI(GenericAPIView, mixins.UpdateModelMixin):
#     serializer_class = WaitingListSerializer
#     queryset = WaitingListUsers.objects.all()
#     lookup_field = 'pk'

#     def put(self, request, pk):
#         try:
#             self.update(request,pk)
#             return JsonResponse({"response":"Update has been successfully!"})
#         except:
#             return JsonResponse({"error":"Bele id-de mehsul tapilmadi"})



        
