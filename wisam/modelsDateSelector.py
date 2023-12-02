from django.db import models
from wisam.modelsDate import Date

class DateSelectors(models.Model):
    date = models.OneToOneField(Date, on_delete=models.CASCADE)
    release_date_selector = models.CharField(max_length=255, default='css-wgsjnl')