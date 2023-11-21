from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from account.renderers import UserRenderer
from rest_framework.permissions import IsAuthenticated,IsAdminUser
import jwt
from .serializers import CartOrderSerializer,CartProductSerializer,PaymentResponseSerializer,PaymentCallbackSerializer
# Create your views here.
from rest_framework_simplejwt.authentication import JWTAuthentication
import random
import string
import time
from .models import CartOrder,CartProduct
from cartorder.utils import Util
# Create your views here.
from rest_framework.decorators import permission_classes, authentication_classes
from rest_framework.decorators import api_view
import requests
from datetime import datetime
import base64

def send_verification_email(email,name,orderid,usertype):

    data = {
        'subject':f"Order Confirmation #{orderid}",
        'to_email':email

    }
    Util.send_email(data,name,orderid,usertype)

def create_order_id():
    timestamp = int(time.time() * 1000)  # Current timestamp in milliseconds
    random_string = ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))  # Random string of length 6
    order_id = f"{timestamp}-{random_string}"
    return order_id


class CreateOrderView(APIView):
    renderer_classes = [UserRenderer]
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]
    def post(self,request,format=None):
        try:
            requested_data  = request.data
            requested_data['order_id'] = create_order_id()
            requested_data['order_status'] = "in progress"
            requested_data['email'] = request.user.email
            
            order_list = requested_data['order_list']
            del requested_data['order_list']
            print(requested_data)
            serializer = CartOrderSerializer(data=requested_data)
            if serializer.is_valid(raise_exception=True):
                value = serializer.save()
                for product_loop in order_list:
                    product_loop['order_id'] = value.id
                    product_loop['total_price']  = product_loop['price'] * product_loop['product_quantity']
                    serializer_products = CartProductSerializer(data=product_loop)
                    if serializer_products.is_valid(raise_exception=True):                        
                        serializer_products.save()


                send_verification_email(request.user.email,requested_data['first_name'],requested_data['order_id'],"user")    
                send_verification_email('alioffice374@gmail.com',requested_data['first_name'],requested_data['order_id'],"admin")
                return Response({'success':'success'},status=status.HTTP_200_OK)
        except Exception as E:
            print(E)
            return Response({'error':'something went wrong'},status=status.HTTP_400_BAD_REQUEST)

class CreateNotLoginOrderView(APIView):    
    def post(self,request,format=None):
        try:
            requested_data  = request.data
            requested_data['order_id'] = create_order_id()
            requested_data['order_status'] = "in progress"
            # requested_data['email'] = request.user.email
            
            order_list = requested_data['order_list']
            del requested_data['order_list']
            print(requested_data)
            serializer = CartOrderSerializer(data=requested_data)
            if serializer.is_valid(raise_exception=True):
                value = serializer.save()
                for product_loop in order_list:
                    product_loop['order_id'] = value.id
                    product_loop['total_price']  = product_loop['price'] * product_loop['product_quantity']
                    serializer_products = CartProductSerializer(data=product_loop)
                    if serializer_products.is_valid(raise_exception=True):                        
                        serializer_products.save()


                send_verification_email(requested_data['email'],requested_data['first_name'],requested_data['order_id'],"user")    
                send_verification_email('alioffice374@gmail.com',requested_data['first_name'],requested_data['order_id'],"admin")
                return Response({'success':'success'},status=status.HTTP_200_OK)
        except Exception as E:
            print(E)
            return Response({'error':'something went wrong'},status=status.HTTP_400_BAD_REQUEST)

class SearchOrderView(APIView):
    # renderer_classes = [UserRenderer]
    # permission_classes = [IsAuthenticated]
    # authentication_classes = [JWTAuthentication]
    def post(self,request,format=None):
        order_id_id = request.data.get('order_id')
        if order_id_id !=None:
            try:
                try:            
                    search_order = CartOrder.objects.get(order_id=order_id_id)
                except:
                    return Response({'success':"not found"},status=status.HTTP_200_OK)

                order_serializer = CartOrderSerializer(search_order)
                order_data = order_serializer.data
                search_product = CartProduct.objects.filter(order_id=order_data['id'])
                product_serializer = CartProductSerializer(search_product,many=True)
                del order_data['id']
                del order_data['email']
                del order_data['payment_type']           
                product_data_list = [{k: v for k, v in item.items() if k not in ['id','order_id']} for item in product_serializer.data]                   
                order_data['products'] = product_data_list
                
                return Response({'success':order_data},status=status.HTTP_200_OK)
            except Exception as E:
                return Response({'error':'something went wrong'},status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({'success':'order id cannot be None'},status=status.HTTP_400_BAD_REQUEST)    


class ChangeOrderStatusView(APIView):    
    renderer_classes = [UserRenderer]
    permission_classes = [IsAuthenticated,IsAdminUser]
    authentication_classes = [JWTAuthentication]

    def get(self,request,format=None):
        try:
            all_search_order = CartOrder.objects.all()
            if len(all_search_order) > 0:
                all_data = []
                order_serializer = CartOrderSerializer(all_search_order,many=True)
                order_data = [dict(item) for item in order_serializer.data]
                search_product = CartProduct.objects.all()
                for order_loop in order_data:
                    search_product = CartProduct.objects.filter(order_id=order_loop['id'])
                    product_serializer = CartProductSerializer(search_product,many=True)
                    product_data_list = [{k: v for k, v in item.items() if k not in ['id']} for item in product_serializer.data]
                    del order_loop['id'] 
                    order_loop['products'] = product_data_list
                    all_data.append(order_loop)
                return Response({'success':all_data},status=status.HTTP_200_OK)
            else:
                return Response({'success':'not order found'},status=status.HTTP_200_OK)

                        
        except:            
            return Response({'error':'something went wrong'},status=status.HTTP_400_BAD_REQUEST)
        
    def patch(self,request,format=None):
        order_id = request.data.get('order_id')
        status_order = request.data.get('order_status')

        if (order_id != None) and (status_order !=None):        
            try:            
                try:                            
                    search_order = CartOrder.objects.get(order_id=order_id)

                except:
                    return Response({'success':"not found"},status=status.HTTP_200_OK)
                
                search_order.order_status = status_order
                search_order.save()
                return Response({'success': "status updated successfully"}, status=status.HTTP_200_OK)
                            
            except:            
                return Response({'error':'something went wrong'},status=status.HTTP_400_BAD_REQUEST)    
        else:
            return Response({'error':'order id and status cannot be None'},status=status.HTTP_200_OK)

class MyOrdersView(APIView):
    renderer_classes = [UserRenderer]
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]

    def get(self,request,format=None):
        try:
            all_my_orders = CartOrder.objects.filter(email=request.user.email)
            all_my_orders_Serializer = CartOrderSerializer(all_my_orders,many=True)
            order_data = [dict(item) for item in all_my_orders_Serializer.data]
            return Response({'success':order_data})
        except Exception as E:
            print(E)
            return Response({'error':'something went wrong'},status=status.HTTP_400_BAD_REQUEST)



@api_view(['GET'])
@permission_classes([IsAuthenticated])
@authentication_classes([JWTAuthentication])
def get_orders_by_car_linkage_id(request, *args, **kwargs):
    linkage_id = request.GET.get('linkageid')
    if linkage_id != None:
        order_table = CartOrder.objects.filter(email=request.user)
        order_table_serialized = CartOrderSerializer(order_table,many=True)
        ids_user = [v['id'] for v in order_table_serialized.data]

        product_table = CartProduct.objects.filter(order_id__in=ids_user).filter(linkageid=linkage_id)
        product_table_serialized = CartProductSerializer(product_table,many=True)

        return Response({'success':product_table_serialized.data},status=status.HTTP_200_OK)
    else:
        return Response({'error':'linkageid cannot be null'},status=status.HTTP_400_BAD_REQUEST)


def get_access_token():
    consumer_key = 'exbuAJUwq02smG5sr6OSDpbSlqto0irc'
    secret_key = 'cTIxXjaGtCdYL4BV'
    access_token_url = 'https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials'
    headers = {'Content-Type': 'application/json'}
    auth = (consumer_key, secret_key)
    try:
        response = requests.get(access_token_url, headers=headers, auth=auth)
        response.raise_for_status()
        result = response.json()
        access_token = result['access_token']
        return access_token        
    except requests.exceptions.RequestException as e:
        return {'error': str(e)}        

@api_view(['POST'])
def payment_response(request, *args, **kwargs):    
    access_token = get_access_token()
    if access_token:
        amount = request.data.get('amount')
        phone = request.data.get('phone')
        if amount!= None and phone!=None:
            passkey = "bfb279f9aa9bdbcf158e97dd71a467cd2e0c893059b10f78e6b72ada1ed2c919"
            business_short_code = '174379'
            process_request_url = 'https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest'
            callback_url = 'https://api.darajambili.com/express-payment'
            timestamp = datetime.now().strftime('%Y%m%d%H%M%S')
            password = base64.b64encode((business_short_code + passkey + timestamp).encode()).decode()
            party_a = phone
            party_b = '254708374149'
            account_reference = 'CompanyXLTD'
            transaction_desc = 'stkpush test'
            stk_push_headers = {
                'Content-Type': 'application/json',
                'Authorization': 'Bearer ' + access_token
            }

            stk_push_payload = {
                'BusinessShortCode': business_short_code,
                'Password': password,
                'Timestamp': timestamp,
                'TransactionType': 'CustomerPayBillOnline',
                'Amount': amount,
                'PartyA': party_a,
                'PartyB': business_short_code,
                'PhoneNumber': party_a,
                'CallBackURL': callback_url,
                'AccountReference': account_reference,
                'TransactionDesc': transaction_desc
            }
            try:
                response = requests.post(process_request_url, headers=stk_push_headers, json=stk_push_payload)
                response.raise_for_status()

                data_insetion = dict()
                data_insetion['merchant_request_id'] = response.json()['MerchantRequestID']
                data_insetion['checkout_request_id'] = response.json()['CheckoutRequestID']
                data_insetion['response_code'] = response.json()['ResponseCode']
                data_insetion['response_description'] = response.json()['ResponseDescription']
                data_insetion['customer_message'] = response.json()['CustomerMessage']

                if response.json()['ResponseCode'] == "0":
                    a=1
                    serializer = PaymentResponseSerializer(data=data_insetion)
                    if serializer.is_valid(raise_exception=True):
                        value = serializer.save()
                        return Response({'success':'success'},status=status.HTTP_200_OK)


                else:
                    return Response({'error':'STK push failed'},status=status.HTTP_400_BAD_REQUEST)
            except requests.exceptions.RequestException as e:
                return Response({'error':e},status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({'error':'amount or phone no is missing'},status=status.HTTP_200_OK)
    else:    
        return Response({'error':'invalid access token'},status=status.HTTP_200_OK)


@api_view(['POST'])
def payment_callback(request, *args, **kwargs):
    received_data = request.data
    if received_data:
        callback = received_data['Body']['stkCallback']
        insertion_callback = dict()

        insertion_callback['merchant_request_id']  = callback['MerchantRequestID']

        insertion_callback['checkout_request_id'] = callback['CheckoutRequestID']

        insertion_callback['result_code'] = callback['ResultCode']

        insertion_callback['result_description'] = callback['ResultDesc']

        
        try:
            for loop in callback['CallbackMetadata']['Item']:
                if loop["Name"] == 'Amount':
                    insertion_callback['amount'] = loop['Value']
                elif loop["Name"] == 'MpesaReceiptNumber':
                    insertion_callback['mpesa_receipt_number'] = loop['Value']
                elif loop["Name"] == 'TransactionDate':
                    insertion_callback['tranaction_date'] = loop['Value']        
                elif loop["Name"] == 'PhoneNumber':
                    insertion_callback['phonenumber'] = loop['Value'] 
        except:            
            insertion_callback['amount'] = None
            insertion_callback['mpesa_receipt_number'] = "N/A"
            insertion_callback['tranaction_date'] = "N/A"
            insertion_callback['phonenumber'] = "N/A"
        try:    
            serializer = PaymentCallbackSerializer(data=insertion_callback)
            if serializer.is_valid(raise_exception=True):
                value = serializer.save()
                return Response({'success':'success'},status=status.HTTP_200_OK)    
        except Exception as E:
            return Response({'error':str(E)},status=status.HTTP_400_BAD_REQUEST)    
                

