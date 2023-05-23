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

# Create your views here.

class UserVehicleView(APIView):
    renderer_classes =[UserRenderer]
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]

    def post(self,request,format=None):
        serializer = UserVehicleSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            deserialized_data = serializer.validated_data
            user = User.objects.get(email=request.user)
            already_exist = UserVehicle.objects.filter(user=user,model=deserialized_data['model'])
            if len(already_exist)<1:
                user_vehicle = UserVehicle(user=user,model=deserialized_data['model'])
                user_vehicle.save()
                return Response({'msg':'vehicle added'}   ,status=status.HTTP_200_OK)
            return Response({'msg':'vehicle already added'}   ,status=status.HTTP_200_OK)

    def get(self,request,format=None):
        user = UserVehicle.objects.filter(user=request.user.id)
        data = []
        for loop in user:
            vehicle = VehicleEngine.objects.get(id=loop.model_id)
            serializer  = VehicleEngineSerializer(vehicle)
            item = dict()
            manufacture_id_id =serializer.data['manufacturer_id']
            man = Manufacturer.objects.get(id=manufacture_id_id)
            serializer_man = ManufacturerSerializer(man)
            manufacturer_id = serializer_man.data['make']
            item['manufacturer_id'] = manufacturer_id
            model_id_id =serializer.data['model_id']
            mod = Model.objects.get(id=model_id_id)

            serializer_mod = ModelSerializer(mod)
            model_id = serializer_mod.data['model']
            item['model_id'] = model_id
            type_year_id_id =serializer.data['type_year_id']
            typ = TypeYear.objects.get(id=type_year_id_id)

            serializer_typ = TypeYearSerializer(typ)
            type_year_id = serializer_typ.data['year']
            item['type_year_id'] = type_year_id

            engine_power_id = serializer.data['engine_power']
            item['engine_power_id'] = engine_power_id
            item['engine_id'] = loop.model_id
            data.append(item)
        return Response(data ,status=status.HTTP_200_OK)
    
    def delete(self,request,format=None):
        serializer = UserVehicleSerializer(data=request.data)
        
        if serializer.is_valid(raise_exception=True):
            deserialized_data = serializer.validated_data
            user = User.objects.get(email=request.user)
            try:
                user_vehicle = UserVehicle.objects.get(user=user,model=deserialized_data['model'])
                user_vehicle.delete()
            except:
                return Response({'msg':'vehicle is not available'} ,status=status.HTTP_200_OK)

            return Response({'msg':'vehicle remove sucessfully'} ,status=status.HTTP_200_OK)
        