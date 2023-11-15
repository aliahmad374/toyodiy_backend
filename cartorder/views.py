from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from account.renderers import UserRenderer
from rest_framework.permissions import IsAuthenticated,IsAdminUser
import jwt
from .serializers import CartOrderSerializer,CartProductSerializer
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
    renderer_classes = [UserRenderer]
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]
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

    