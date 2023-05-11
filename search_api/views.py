from django.shortcuts import render

from rest_framework.views import APIView
from .models import Manufacturer,Model,TypeYear,VehicleEngine,Category,SubCategory,Parts
from .serializers import ManufacturerSerializer,ModelSerializer,TypeYearSerializer,VehicleEngineSerializer,CategorySerializer,SubCategorySerializer,PartsSerializer
from rest_framework.response import Response

# Create your views here.

class ManufactureAPI(APIView):
    def get(self,request,format=None):
        # parameters = request.query_params.get('manufacturer_id', None)
        # if parameters is not None:
        #     make = Manufacturer.objects.get(id=parameters)
        #     serializer = ManufacturerSerializer(make)
        #     return Response(serializer.data)

        make = Manufacturer.objects.all()
        serializer = ManufacturerSerializer(make, many=True)
        return Response(serializer.data)
        



class ModelAPI(APIView):
    def get(self,request,format=None):        
        parameter = request.query_params.get('manufacturer_id', None)
        if parameter is not None:
            try:
                model = Model.objects.filter(manufacturer_id=parameter)
                serializer  = ModelSerializer(model,many=True)
                return Response(serializer.data)
            except:
                return Response({'error':'not found'})

        # model = Model.objects.all()
        # serializer = ModelSerializer(model,many=True)
        # return Response(serializer.data)
    
class Type_YearAPI(APIView):    
    def get(self,request,format=None):        
        manufacture_parameter = request.query_params.get('manufacturer_id', None)
        model_parameter = request.query_params.get('model_id', None)

        try:
            if manufacture_parameter is not None and model_parameter is not None:
                year = TypeYear.objects.filter(manufacturer_id=manufacture_parameter,model_id=model_parameter)
                serializer  = TypeYearSerializer(year,many=True)
                return Response(serializer.data)
        except:
            return Response({'error':'not found'})    
        # year = TypeYear.objects.all()
        # serializer = TypeYearSerializer(year,many=True)
        # return Response(serializer.data)


    

class VehicleAPI(APIView):
    def get(self,request,format=None):
        manufacture_parameter = request.query_params.get('manufacturer_id', None)
        model_parameter = request.query_params.get('model_id', None)       
        year_parameter = request.query_params.get('year_id', None)       

        try:
            if manufacture_parameter is not None and model_parameter is not None and year_parameter is not None:
                vehicle = VehicleEngine.objects.filter(manufacturer_id=manufacture_parameter,model_id=model_parameter,type_year_id=year_parameter)
                serializer  = VehicleEngineSerializer(vehicle,many=True)
                return Response(serializer.data)
        except:
            return Response({'error':'not found'})    
        # vehicle = VehicleEngine.objects.all()
        # serializer = VehicleEngineSerializer(vehicle,many=True)
        # return Response(serializer.data)
    
class CategoryAPI(APIView):
    def get(self,request,format=None):                       
        # manufacture_parameter = request.query_params.get('manufacturer_id', None)
        # model_parameter = request.query_params.get('model_id', None)       
        # year_parameter = request.query_params.get('year_id', None)
        # vehicle_parameter = request.query_params.get('engine_id', None)

        # try:
        #     if manufacture_parameter is not None and model_parameter is not None and year_parameter is not None and vehicle_parameter is not None:
        #         category = Category.objects.filter(manufacturer_id=manufacture_parameter,model_id=model_parameter,type_year_id=year_parameter,vehicle_id=vehicle_parameter)
        #         serializer  = CategorySerializer(category,many=True)
        #         return Response(serializer.data)
        # except:
        #     return Response({'error':'not found'})    
        category = Category.objects.all()
        serializer = CategorySerializer(category,many=True)
        return Response(serializer.data)

class SubCategoryAPI(APIView):
    def get(self,request,format=None,pk=None):        
        category_parameter = request.query_params.get('category_id', None)
        try:
            if category_parameter is not None:
                subcategory = SubCategory.objects.filter(category_id=category_parameter)
                serializer  = SubCategorySerializer(subcategory,many=True)
                return Response(serializer.data)
        except:
            return Response({'error':'not found'})    
        # subcategory = SubCategory.objects.all()
        # serializer = SubCategorySerializer(subcategory,many=True)
        # return Response(serializer.data)
    
class PartsAPI(APIView):    
    def get(self,request,format=None,pk=None):        
        try:
            subcategory_parameter = request.query_params.get('subcategory_id', None)
            engine_parameter = request.query_params.get('engine_id', None)
            if (subcategory_parameter is not None) and (engine_parameter is not None):
                part = Parts.objects.filter(sub_category_id=subcategory_parameter,engine_power=engine_parameter)
                serializer  = PartsSerializer(part,many=True)
                return Response([{'id':v.get('id'),'name':v.get('part_name')} for v in serializer.data])
            if (subcategory_parameter is not None) and (engine_parameter == None):
                part = Parts.objects.filter(sub_category_id=subcategory_parameter)
                serializer  = PartsSerializer(part,many=True)
                return Response([{'id':v.get('id'),'name':v.get('part_name')} for v in serializer.data])
            
        except Exception as e:            
            return Response({'error':'not found'})
    

class PartsDetailAPI(APIView):
    def get(self,request,format=None,pk=None):        
        part_parameter = request.query_params.get('part_id', None)
        try:
            if part_parameter is not None:
                part = Parts.objects.get(id=part_parameter)
                serializer  = PartsSerializer(part)
                return Response(serializer.data)
        except:
            return Response({'error':'not found'})    
        
class PartsNumberAPI(APIView):
    def get(self,request,format=None,pk=None):        
        part_parameter = request.query_params.get('part_number', None)
        try:
            if part_parameter is not None:
                part = Parts.objects.filter(part_number=part_parameter)
                serializer  = PartsSerializer(part,many=True)
                return Response([{'id':v.get('id'),'part_number':v.get('part_number')} for v in serializer.data])
        except:
            return Response({'error':'not found'})    


class AutoComplete(APIView):        
        def get(self,request,format=None,pk=None):                
            text_parameter = request.query_params.get('text', None)
            try:
                if text_parameter is not None:
                    part = Parts.objects.filter(part_number__istartswith=text_parameter)
                    serializer  = PartsSerializer(part,many=True)
                    # return Response([{'id':v.get('id'),'part_number':v.get('part_number')} for v in serializer.data])
                    return Response(serializer.data[:10])
            except:
                return Response({'error':'not found'})    


