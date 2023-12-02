from django.db import models
from wisam.modelShoes import Shoes

class Color(models.Model):
    shoes = models.ForeignKey(Shoes, on_delete=models.CASCADE)
    color = models.CharField(max_length=100)
    material = models.CharField(max_length=100)
    weight_of_shoe = models.DecimalField(max_digits=4, decimal_places=2)