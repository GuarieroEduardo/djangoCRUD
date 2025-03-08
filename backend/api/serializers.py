from rest_framework import serializers

from .models import *

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustonUser
        fields = '__all__'
    