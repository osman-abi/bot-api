from .models import User
from .serializers import UserSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import GenericAPIView

# Create your views here.



class UserAuthAPI(GenericAPIView):

    serializer_class = UserSerializer
    queryset = User.objects.all()

    def get(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)