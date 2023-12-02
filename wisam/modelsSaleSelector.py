from django.db import models
from wisam.modelShoes import Sales

class SalesSelectors(models.Model):
    sales = models.OneToOneField(Sales, on_delete=models.CASCADE)
    number_sold_last_3_days_selector = models.CharField(max_length=255, default='css-6zmw74')