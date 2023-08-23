from django.contrib import admin
from .models import CartOrder,CartProduct


# Register your models here.
@admin.register(CartOrder)
class CartOrdereAdmin(admin.ModelAdmin):
    list_display = ['id','order_id','date_of_purchase','order_status','email','first_name','last_name','phone','shipping_address','city','postal_code','payment_type']
@admin.register(CartProduct)
class CartProductAdmin(admin.ModelAdmin):
    list_display = ['id','order_id','product_name','product_manufacture','product_type','product_model','product_quantity','price','product_id','total_price']