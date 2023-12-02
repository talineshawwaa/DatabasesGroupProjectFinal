from django.db import models
from wisam.modelsColor import Color

class ColorSelectors(models.Model):
    color = models.OneToOneField(Color, on_delete=models.CASCADE)
    colorway_selector = models.CharField(max_length=255, default='css-wgsjnl')