from django.db import models


class quality_model1(models.Model):
    username = models.CharField(max_length=200)
    email = models.EmailField(unique=True)
    phonenumber = models.PositiveBigIntegerField(null=True)
    gender = models.CharField(max_length=200, null=True)
    address = models.CharField(max_length=200, null=True)
    password = models.CharField(max_length=200)



























class raw_materials(models.Model):
    iron_ore = models.PositiveBigIntegerField(null=True)
    coking_coal = models.PositiveBigIntegerField(null=True)
    ferrous_scrap = models.PositiveBigIntegerField(null=True)
    manganese = models.PositiveBigIntegerField(null=True)
    siliconferro_alloy = models.PositiveBigIntegerField(null=True)
    chromium = models.PositiveBigIntegerField(null=True)
    nickel = models.PositiveBigIntegerField(null=True)
    zinc = models.PositiveBigIntegerField(null=True)
    tin = models.PositiveBigIntegerField(null=True)
    molybdenum = models.PositiveBigIntegerField(null=True)
    vanadium = models.PositiveBigIntegerField(null=True)
    TUNGSTEN = models.PositiveBigIntegerField(null=True)

class quality_team(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(unique=True)
    gender = models.CharField(max_length=200, null=True)
    address = models.CharField(max_length=200, null=True)
    employee_id = models.CharField(max_length=200, null=True)
    Supplier = models.CharField(max_length=200, null=True)
    inspection_team_type = models.CharField(max_length=200, null=True)
    raw_material_quality = models.CharField(max_length=200, null=True)