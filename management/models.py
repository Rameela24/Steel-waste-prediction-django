from django.db import models

# Create your models here.
class management_model1(models.Model):
    username = models.CharField(max_length=200)
    email = models.EmailField(unique=True)
    phonenumber = models.PositiveBigIntegerField(null=True)
    gender = models.CharField(max_length=200, null=True)
    address = models.CharField(max_length=200, null=True)
    password = models.CharField(max_length=200)