from rest_framework import serializers

from .models import CartOrder,CartProduct


class CartOrderSerializer(serializers.ModelSerializer): 
    class Meta:
        model=CartOrder
        fields = ['id','order_id','date_of_purchase','order_status','payment_type','email','first_name','last_name','phone','shipping_address','city','postal_code']


class CartProductSerializer(serializers.ModelSerializer): 
    class Meta:
        model=CartProduct
        fields = ['id','order_id','product_name','product_manufacture','product_type','product_model','product_quantity','price','product_id','total_price','itemid','group4','stkgencode','linkageid']

