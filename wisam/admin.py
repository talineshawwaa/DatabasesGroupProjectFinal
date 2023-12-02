from django.contrib import admin
from wisam.modelShoes import Shoes
from wisam.modelsManufacturer import Manufacturer 
from wisam.modelsColor import Color
from wisam.modelsDate import Date
from wisam.modelsSales import Sales 
from wisam.modelsShoeSelector import ShoeSelectors 
from wisam.modelsManufacturerSelectors import ManufacturerSelectors
from wisam.modelsColorSelector import ColorSelectors
from wisam.modelsDateSelector import DateSelectors
from wisam.modelsSaleSelector import SalesSelectors

# Register your models here.
class ShoesAdmin(admin.ModelAdmin):
    list_display = ['brand','model_name', 'size', 'price']

class ManufacturerAdmin(admin.ModelAdmin):
    list_display = ['brand','model_name', 'size', 'price']

class ColorAdmin(admin.ModelAdmin):
    list_display = ['shoes','color', 'material', 'weight_of_shoe']

class DateAdmin(admin.ModelAdmin):
    list_display = ['shoes','release_date', 'season', 'weight_of_shoe', 'reviews']

class SalesAdmin(admin.ModelAdmin):
    list_display = ['shoes', 'number_sold_last_3_days']

class ShoeSelectorsAdmin(admin.ModelAdmin):
    list_display = ['shoe', 'brand_selector', 'model_name_selector', 'size_selector', 'price_selector']

class ManufacturerSelectorsAdmin(admin.ModelAdmin):
    list_display = ['manufacturer', 'name_selector', 'retail_price', 'price_increase']

class ColorSelectorsAdmin(admin.ModelAdmin):
    list_display = ['color', 'colorway_selector']

class DateSelectorsAdmin(admin.ModelAdmin):
    list_display = ['date', 'release_date_selector']

class SalesSelectorAdmin(admin.ModelAdmin):
    list_display = ['shoes', 'number_sold_last_3_days_selector']


admin.site.register(Shoes,ShoesAdmin)
admin.site.register(Manufacturer,ManufacturerAdmin)
admin.site.register(Color,ColorAdmin)
admin.site.register(Date,DateAdmin)
admin.site.register(Sales,DateAdmin)
admin.site.register(ShoeSelectors,ShoeSelectorsAdmin)
admin.site.register(ManufacturerSelectors,ManufacturerSelectorsAdmin)
admin.site.register(ColorSelectors,ColorSelectorsAdmin)
admin.site.register(DateSelectors,DateSelectorsAdmin)
admin.site.register(SalesSelectors,SalesSelectorAdmin)