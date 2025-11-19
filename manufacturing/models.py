from django.db import models


class manufacturing_model1(models.Model):
    username = models.CharField(max_length=200)
    email = models.EmailField(unique=True)
    phonenumber = models.PositiveBigIntegerField(null=True)
    gender = models.CharField(max_length=200, null=True)
    address = models.CharField(max_length=200, null=True)
    password = models.CharField(max_length=200)

class manufacturing_process(models.Model):
    iron_making = models.CharField(max_length=200)
    primary_steel_making = models.CharField(max_length=200)
    secondary_steel_making = models.CharField(max_length=200)
    casting = models.CharField(max_length=200)
    first_forming = models.CharField(max_length=200)
    fabrication = models.CharField(max_length=200)
    finishing = models.CharField(max_length=200)
    final = models.CharField(max_length=200, null=True)
    approve = models.BooleanField(default=False)

class expected_ot(models.Model):
    iron_ore = models.CharField(max_length=200)
    COKING_COAL = models.CharField(max_length=200)
    FERROUS_SCRAP = models.CharField(max_length=200)
    METHOD = models.CharField(max_length=200)
    OUTPUT = models.CharField(max_length=200,null=True)
    WASTE = models.CharField(max_length=200,null=True)




