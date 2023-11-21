from rest_framework import serializers

from .models import CartOrder,CartProduct,payment_response,payment_callback


class CartOrderSerializer(serializers.ModelSerializer): 
    class Meta:
        model=CartOrder
        fields = ['id','order_id','date_of_purchase','order_status','payment_type','email','first_name','last_name','phone','shipping_address','city','postal_code']


class CartProductSerializer(serializers.ModelSerializer): 
    class Meta:
        model=CartProduct
        fields = ['id','order_id','product_name','product_manufacture','product_type','product_model','product_quantity','price','product_id','total_price','itemid','group4','stkgencode','linkageid']


class PaymentResponseSerializer(serializers.ModelSerializer): 
    class Meta:
        model=payment_response
        fields = ['id','merchant_request_id','checkout_request_id','response_code','response_description','customer_message']

class PaymentCallbackSerializer(serializers.ModelSerializer): 
    class Meta:
        model=payment_callback
        fields = ['id','merchant_request_id','checkout_request_id','result_code','result_description','amount','mpesa_receipt_number','tranaction_date','phonenumber']        