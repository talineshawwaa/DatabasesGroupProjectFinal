from django.db import models
from wisam.modelShoes import Shoes

class Date(models.Model):
    shoes = models.ForeignKey(Shoes, on_delete=models.CASCADE)
    release_date = models.DateField()
