from django.db import models
from wisam.modelShoes import Shoes

class Sales(models.Model):
    shoes = models.ForeignKey(Shoes, on_delete=models.CASCADE)
    number_sold_last_3_days = models.IntegerField()