from unicodedata import name
from django.shortcuts import render
from rest_framework.views import APIView
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.generics import GenericAPIView
from rest_framework import mixins
from contact.models import Contacts
import requests
import json
# Create your views here.

ACCESS_TOKEN = 'EAAIyUoMs63QBAPl1adF7Pc0jR1v8PunjjrJ30ARUS0qUCVubJt27TM6xu9hIZCQV6ZBXa9dts2nz8CYrlromXl81HfPkTFzPDVo0vypRFMfXM0IO8vpUwwswMM1FZBTi4Yg9rYExexyF6SVUmEZAsmiyodnYJCsHZBho04BDYJKZB9RhNZAZAXy34Enxu3pZC9ToZD'
PAGE_ID = 106018905364086

def post_facebook_message(fbid, recevied_message):
    post_message_url = 'https://graph.facebook.com/v13.0/me/messages?access_token={}'.format(ACCESS_TOKEN)
    response_msg = json.dumps({"recipient":{"id":fbid}, "message":{"text":recevied_message}})
    status = requests.post(post_message_url, headers={"Content-Type": "application/json"},data=response_msg)
    print(status.json())
    return status.json()


class FacebookBotView(APIView):

    def get(self,request):
        if request.GET.get('hub.verify_token') == 'testotomall':
            return JsonResponse({'response':request.GET.get('hub.challenge')})
        else:
            return JsonResponse({'response':'token dogru deyil'})

    def post(self, request):
        incoming_message = json.loads(request.body.decode('utf-8'))
        print('incoming message -> ',incoming_message)
        sender_id = None
        msj = None

        if incoming_message['object'] == 'page':
            for entry in incoming_message['entry']:
                for message in entry.get('messaging'):
                    if 'message' in message:
                        msj = message
                        print('MESSAGE -> ',message)
                        sender_id = message['sender']['id']
        
        elif incoming_message['object'] == 'admin':
            for entry in incoming_message['entry']:
                for message in entry.get('messaging'):
                    if 'message' in message:
                        msj = message
                        post_facebook_message(message['sender']['id'],message['message']['text'])
            
        r = requests.get('https://graph.facebook.com/v13.0/{}?fields=first_name,last_name,gender,profile_pic&access_token={}'.format(sender_id,ACCESS_TOKEN))
        account = r.json()
        if not Contacts.objects.filter(sender_id=sender_id).exists():
            Contacts.objects.create(
                avatar = account.get('profile_pic'),
                sender_id = sender_id,
                name = account.get('first_name'),
                surname = account.get('last_name'),
                gender = account.get('gender')
            )

        return JsonResponse({'message':msj})