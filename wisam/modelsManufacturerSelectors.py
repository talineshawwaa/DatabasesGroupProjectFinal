from django.db import models
from wisam.modelShoes import Shoes
from wisam.modelsManufacturer import Manufacturer

class ManufacturerSelectors(models.Model):
    manufacturer = models.OneToOneField(Manufacturer, on_delete=models.CASCADE)
    name_selector = models.CharField(max_length=255, default='css-t7k2e1')
    retail_price = models.CharField(max_length=255, default='css-wgsjnl')
    price_increase = models.CharField(max_length=255, default='css-17b7qhr')