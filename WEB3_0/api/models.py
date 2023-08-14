from django.core.validators import MinLengthValidator
from django.db import models, transaction


class User_Model(models.Model):
    User_Name = models.CharField(max_length=15, )
    User_IIN = models.CharField(max_length=12, validators=[MinLengthValidator(12)], unique=True)
    All_money = models.DecimalField(default=0, max_digits=100, decimal_places=2)

    def __str__(self) -> object:
        return f"{self.User_Name} {self.All_money}"
