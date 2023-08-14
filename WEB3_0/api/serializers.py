from django.core.validators import MinLengthValidator
from rest_framework import serializers

from .models import User_Model


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User_Model
        fields = '__all__'


class MoneyTransferSerializer(serializers.Serializer):
    source_inn = serializers.CharField(max_length=12, validators=[MinLengthValidator(12)])
    target_inn = serializers.CharField(max_length=12, validators=[MinLengthValidator(12)])
    amount = serializers.DecimalField(default=0, max_digits=100, decimal_places=2)
