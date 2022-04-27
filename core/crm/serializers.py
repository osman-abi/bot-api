from rest_framework.serializers import ModelSerializer
from .models import CallMeUsers, CarBuyerUsers, WaitingListUsers


class CallMeSerializer(ModelSerializer):
    class Meta:
        model  = CallMeUsers
        fields = '__all__'

class CarBuyerSerializer(ModelSerializer):
    class Meta:
        model  = CarBuyerUsers
        fields = '__all__'

class WaitingListSerializer(ModelSerializer):
    class Meta:
        model  = WaitingListUsers
        fields = '__all__'