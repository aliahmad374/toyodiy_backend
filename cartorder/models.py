from django.db import models

class CartOrder(models.Model):
    order_id = models.CharField(max_length=30, unique=True)
    date_of_purchase = models.DateTimeField(auto_now_add=True)
    order_status = models.TextField()
    payment_type = models.TextField()
    email = models.EmailField()
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    phone = models.CharField(max_length=30)
    shipping_address = models.TextField()
    city = models.CharField(max_length=50)
    postal_code = models.CharField(max_length=10)
    def __str__(self):
        return self.order_id
    
    class Meta:
        db_table = 'orders'
class CartProduct(models.Model):
    order_id = models.ForeignKey(CartOrder, on_delete=models.CASCADE)
    product_name = models.TextField()
    product_manufacture = models.TextField()
    product_type = models.TextField()
    product_model = models.TextField()
    product_quantity = models.PositiveIntegerField()
    total_price = models.DecimalField(max_digits=20, decimal_places=5)
    price = models.DecimalField(max_digits=20, decimal_places=2)
    product_id = models.CharField(max_length=30)  # Assuming product_id is a unique identifier
    itemid = models.CharField(max_length=40)
    group4 = models.CharField(max_length=40)
    stkgencode = models.CharField(max_length=40)
    linkageid = models.CharField(max_length=40)
    def __str__(self):
        return f"{self.product_name} - {self.order.order_id}"
    class Meta:
        db_table = 'products'

class payment_response(models.Model):
    merchant_request_id = models.CharField(max_length=50)
    checkout_request_id = models.CharField(max_length=50)
    response_code = models.CharField(max_length=10)
    response_description = models.TextField()
    customer_message = models.TextField()
    class Meta:
        db_table = 'PaymentResponse'


class payment_callback(models.Model):
    merchant_request_id = models.CharField(max_length=50)
    checkout_request_id = models.CharField(max_length=50)
    result_code = models.CharField(max_length=10)
    result_description = models.TextField()
    amount = models.DecimalField(max_digits=20, decimal_places=5, null=True)
    mpesa_receipt_number = models.TextField()
    tranaction_date = models.TextField()
    phonenumber = models.TextField()
    class Meta:
        db_table = 'PaymentCallback'