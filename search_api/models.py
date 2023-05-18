# Create your models here.

from django.db import models


class Category(models.Model):
    category_name = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'category'


class Manufacturer(models.Model):
    make = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'manufacturer'


class Model(models.Model):
    manufacturer = models.ForeignKey(Manufacturer, models.DO_NOTHING, blank=True, null=True)
    model = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'model'


class Parts(models.Model):
    sub_category = models.ForeignKey('SubCategory', models.DO_NOTHING, blank=True, null=True)
    engine_code = models.TextField(blank=True, null=True)
    market = models.TextField(blank=True, null=True)
    part_number = models.TextField(blank=True, null=True)
    part_name = models.TextField(blank=True, null=True)
    quantity_required = models.IntegerField(blank=True, null=True)
    part_source = models.TextField(blank=True, null=True)
    price = models.FloatField(blank=True, null=True)
    engine_power_id = models.ForeignKey('VehicleEngine', models.DO_NOTHING, blank=True, null=True,db_column='engine_power_id')

    class Meta:
        managed = False
        db_table = 'parts'


class SubCategory(models.Model):
    category = models.ForeignKey(Category, models.DO_NOTHING, blank=True, null=True)
    sub_category_name = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sub_category'


class TypeYear(models.Model):
    manufacturer = models.ForeignKey(Manufacturer, models.DO_NOTHING, blank=True, null=True)
    model = models.ForeignKey(Model, models.DO_NOTHING, blank=True, null=True)
    year = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'type_year'


class VehicleEngine(models.Model):
    id = models.AutoField(primary_key=True)
    manufacturer = models.ForeignKey(Manufacturer, models.DO_NOTHING, blank=True, null=True)
    model = models.ForeignKey(Model, models.DO_NOTHING, blank=True, null=True)
    type_year = models.ForeignKey(TypeYear, models.DO_NOTHING, blank=True, null=True)
    engine_power = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'vehicle_engine'
