from rest_framework import serializers
from .models import User_Model


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User_Model
        fields = '__all__'


class MoneyTransferSerializer(serializers.Serializer):
    source_inn = serializers.CharField()
    target_inn = serializers.CharField()
    amount = serializers.FloatField(default=0)
