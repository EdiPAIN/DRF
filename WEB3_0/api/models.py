from django.db import models, transaction
from django.conf import settings


class User_Model(models.Model):
    User_Name = models.CharField(max_length=15, )
    User_IIN = models.CharField(max_length=12, unique=True)
    All_money = models.FloatField(default=0)

    def __str__(self) -> object:
        return f"{self.User_Name} {self.All_money}"

