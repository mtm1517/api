from django.contrib import admin
from .models import Product, Catelogy, Shipping, Order, Rating

# Register your models here.
#admin.site.register(Product)
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'price', 'id_catelogy', 'status']
    list_filter = ['id_catelogy']
    search_fields = ['title']

admin.site.register(Catelogy)
admin.site.register(Shipping)
#admin.site.register(Order)
@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'total_items', 'total_amount', 'id_shipping']
    search_fields = ['total_amount']

admin.site.register(Rating)