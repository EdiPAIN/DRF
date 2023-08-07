from rest_framework import serializers
from .models import User_Model


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User_Model
        fields = '__all__'

class MoneyTransferSerializer(serializers.Serializer):
    source_inn = serializers.IntegerField()
    target_inn = serializers.ListField()
    amount = serializers.FloatField()


