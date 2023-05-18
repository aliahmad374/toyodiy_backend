from django.contrib import admin
from .models import UserVehicle
# Register your models here.

@admin.register(UserVehicle)
class UserVehicleAdmin(admin.ModelAdmin):
    list_display = ['id','model_id','user_id']