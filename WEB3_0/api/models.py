from django.core.validators import MinLengthValidator
from django.db import models, transaction
from django.core.exceptions import ValidationError


class User_Model(models.Model):
    User_Name = models.CharField(max_length=15, )
    User_IIN = models.CharField(max_length=12,validators=[MinLengthValidator(12)], unique=True)
    All_money = models.FloatField(default=0)

    def only_int(value):
        if value.isdigit() == False:
            raise ValidationError('IIN contains characters')

    def __str__(self) -> object:
        return f"{self.User_Name} {self.All_money}"
