from rest_framework.serializers import ModelSerializer
from .models import Contacts, ReplyMessage

class ContactSerializer(ModelSerializer):
    class Meta:
        model = Contacts
        fields = '__all__' 


class ReplyMessageSerializer(ModelSerializer):
    class Meta:
        model = ReplyMessage
        fields = '__all__' 

