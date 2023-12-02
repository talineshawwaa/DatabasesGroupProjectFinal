from django.db import models

class Shoes(models.Model):
    model_name = models.CharField(max_length=50)
    brand = models.CharField(max_length=50)
    sizes = models.ArrayField(models.DecimalField(max_digits=4, decimal_places=2))
    price = models.DecimalField(max_digits=10, decimal_places=2)
    color_description = models.CharField(max_length=50, blank=True, null=True)
    model_number = models.CharField(max_length=50, blank=True, null=True)