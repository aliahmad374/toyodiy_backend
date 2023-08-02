from rest_framework import serializers

from .models import Eztb3105


class Eztb3105Serializer(serializers.ModelSerializer): 
    class Meta:
        model=Eztb3105
        fields = '__all__'