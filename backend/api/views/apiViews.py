from rest_framework import viewsets
from api.models import *
from api.serializers import *

class UseerViewSet(viewsets.ModelViewSet):
    queryset = CustonUser.objects.all()
    serializer_class = UserSerializer