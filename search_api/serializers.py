from rest_framework import serializers

from .models import Category,SubCategory,VehicleEngine,TypeYear,Model,Manufacturer,Parts


class CategorySerializer(serializers.ModelSerializer): 
    class Meta:
        model=Category
        fields = ['id','category_name']

class SubCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model=SubCategory
        fields = ['id','category_id','sub_category_name']

class VehicleEngineSerializer(serializers.ModelSerializer): 
    class Meta:
        model=VehicleEngine
        fields = ['id','manufacturer_id','model_id','type_year_id','engine_power']


class TypeYearSerializer(serializers.ModelSerializer):
    class Meta:
        model=TypeYear
        fields = ['id','manufacturer_id','model_id','year']

class ModelSerializer(serializers.ModelSerializer): 
    class Meta:
        model=Model
        fields = ['id','manufacturer_id','model']

class ManufacturerSerializer(serializers.ModelSerializer): 
    class Meta:
        model=Manufacturer
        fields = ['id','make']

class PartsSerializer(serializers.ModelSerializer): 
    class Meta:
        model=Parts
        fields = ['id','sub_category_id','engine_code','market','part_number','part_name','quantity_required','part_source','price','engine_power']