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
                try:
                    part = Parts.objects.filter(sub_category_id=subcategory_parameter,engine_power_id__id=engine_parameter)
                except Exception as E:
                    return Response({'error':'part not found'})
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
                first_matched = [{'id':v.get('id'),'part_number':v.get('part_number'),'engine_power_id':v.get('engine_power_id')} for v in serializer.data[0:1]]

                other_fits_parts = []
                done_part = []
                for other_fit in serializer.data[1:]:
                    item = dict()
                    
                    item['id'] = other_fit.get('id')
                    item['part_number'] = other_fit.get('part_number')
                    item['engine_power_id'] = other_fit.get('engine_power_id')
                    if (item['engine_power_id'] != first_matched[0]['engine_power_id'] ) and (item['engine_power_id'] not in done_part):
                        vehicle_engine_power = VehicleEngine.objects.get(id=item['engine_power_id'])
                        serializer = VehicleEngineSerializer(vehicle_engine_power)
                        model_name_id = serializer.data.get('model_id')
                        item['engine_power'] = serializer.data.get('engine_power')
                        item['model_id'] = model_name_id
                        model_name_object = Model.objects.get(id= model_name_id)
                        model_name_serializer  = ModelSerializer(model_name_object)
                        item['name'] = model_name_serializer.data.get('model')
                        
                        year_id = serializer.data.get('type_year_id')
                        item['year_id'] = year_id
                        year_name_object = TypeYear.objects.get(id=year_id)
                        year_serializer = TypeYearSerializer(year_name_object)
                        item['year'] = year_serializer.data.get('year')
                        other_fits_parts.append(item)
                        done_part.append(item['engine_power_id'])
                return Response({'first_matched':first_matched,'other fits':other_fits_parts})
        except:
            return Response({'error':'not found'})    


class AutoComplete(APIView):        
        def get(self,request,format=None,pk=None):                
            text_parameter = request.query_params.get('text', None)
            try:
                if text_parameter is not None:
                    part = Parts.objects.filter(part_number__istartswith=text_parameter)
                    serializer  = PartsSerializer(part,many=True)
                    return Response([{'id':v.get('id'),'part_number':v.get('part_number'),'part_name':v.get('part_name')} for v in serializer.data[:10]])
            except:
                return Response({'error':'not found'})    


