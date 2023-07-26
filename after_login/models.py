from django.db import models
from account.models import User
from search_api.models import VehicleEngine
# Create your models here.

class UserVehicle(models.Model):
     user = models.ForeignKey(User, on_delete=models.CASCADE,related_name='vehicle_user')
     # model = models.ForeignKey(VehicleEngine, on_delete=models.CASCADE,related_name='model_user',to_field='id',db_column='model_id')
     model_id = models.TextField(blank=False, null=False,db_column='model_id')
     class Meta:
            db_table = 'UserVehicle'
