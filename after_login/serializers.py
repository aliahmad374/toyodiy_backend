from rest_framework import serializers
from .models import UserVehicle


class UserVehicleSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserVehicle
        fields = ['model_id']