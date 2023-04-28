# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
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
    engine_power = models.ForeignKey('VehicleEngine', models.DO_NOTHING, blank=True, null=True)

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
    manufacturer = models.ForeignKey(Manufacturer, models.DO_NOTHING, blank=True, null=True)
    model = models.ForeignKey(Model, models.DO_NOTHING, blank=True, null=True)
    type_year = models.ForeignKey(TypeYear, models.DO_NOTHING, blank=True, null=True)
    engine_power = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'vehicle_engine'
