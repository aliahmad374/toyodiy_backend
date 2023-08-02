from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from account.renderers import UserRenderer
from rest_framework.permissions import IsAuthenticated
from .serializers import UserVehicleSerializer
from .models import UserVehicle
# Create your views here.
from rest_framework_simplejwt.authentication import JWTAuthentication
from account.models import  User

from search_api.models import Manufacturer,Model,TypeYear,VehicleEngine
from search_api.serializers import ManufacturerSerializer,ModelSerializer,TypeYearSerializer,VehicleEngineSerializer
import requests
import json
# Create your views here.

class UserVehicleView(APIView):
    renderer_classes =[UserRenderer]
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]

    def post(self,request,format=None):        
        serializer = UserVehicleSerializer(data=request.data)        
        if serializer.is_valid(raise_exception=True):
            deserialized_data = serializer.validated_data
            print('----------------------------------------------')
            print(deserialized_data)
            print('----------------------------------------------')

            user = User.objects.get(email=request.user)
            print(user)
            total_cars = UserVehicle.objects.filter(user=user)
            if len(total_cars)==2:               
                return Response({'msg':'You have reached your limit to add vehicle'}   ,status=status.HTTP_200_OK)
            
            already_exist = UserVehicle.objects.filter(user=user,model_id=deserialized_data['model_id'])
            if len(already_exist)<1:
                user_vehicle = UserVehicle(user=user,model_id=deserialized_data['model_id'])
                user_vehicle.save()
                return Response({'msg':'vehicle added'}   ,status=status.HTTP_200_OK)
            
            
            return Response({'msg':'vehicle already added'}   ,status=status.HTTP_200_OK)

    def get(self,request,format=None):
        user = UserVehicle.objects.filter(user=request.user.id)
        se = UserVehicleSerializer(user,many=True)
        all_vehicle = []
        authorization_header = f"{request.META.get('HTTP_AUTHORIZATION')}"

        headers = {
            'Authorization':authorization_header
        }
        for loop in se.data:
            print(loop['model_id'])
            url= f"http://127.0.0.1:8000/techdoc/sidebar/?linkageTargetIds="+str(int(loop['model_id']))
            all_vehicle.append(json.loads(requests.get(url=url,headers=headers).text))

        return Response({'msg':all_vehicle} ,status=status.HTTP_200_OK)
    
    def delete(self,request,format=None):
        serializer = UserVehicleSerializer(data=request.data)
        
        if serializer.is_valid(raise_exception=True):
            deserialized_data = serializer.validated_data
            user = User.objects.get(email=request.user)
            try:
                user_vehicle = UserVehicle.objects.get(user=user,model_id=deserialized_data['model_id'])
                user_vehicle.delete()
            except:
                return Response({'msg':'vehicle is not available'} ,status=status.HTTP_200_OK)

            return Response({'msg':'vehicle remove sucessfully'} ,status=status.HTTP_200_OK)
        