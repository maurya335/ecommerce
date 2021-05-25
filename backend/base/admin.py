from django.contrib import admin
from .models import *
# Register your models here.

# admin.site.register(Product)
admin.site.register(Review)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(ShippingAddress)



@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
 list_display=['user', 'name', 'image', 'brand','category','description','rating','numReviews','price','countInStock','createAt','_id']