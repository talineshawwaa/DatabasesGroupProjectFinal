from django.db import models
from wisam.modelShoes import Shoes

class Manufacturer(models.Model):
    shoes = models.ForeignKey(Shoes, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    price_increase = models.CharField(max_length=50)
    retail_price = models.CharField(max_length=50)