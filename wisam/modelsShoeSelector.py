from django.db import models
from wisam.modelShoes import Shoes

class ShoeSelectors(models.Model):
    shoe = models.OneToOneField(Shoes, on_delete=models.CASCADE)
    brand_selector = models.CharField(max_length=255, default='css-t7k2e1')
    model_name_selector = models.CharField(max_length=255, default='css-t7k2e1')
    size_selector = models.CharField(max_length=255, default='css-r6z5ec')
    price_selector = models.CharField(max_length=255, default='css-cptlwn')