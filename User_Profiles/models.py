from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class User_Profiles(models.Model): 
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    phone= models.CharField(max_length=200,blank=True)
    address_1= models.CharField(max_length=200,blank=True)
    address_2= models.CharField(max_length=200,blank=True)
    country= models.CharField(max_length=60,blank=True)
    city= models.CharField(max_length=60,blank=True)
    state= models.CharField(max_length=60,blank=True)
    zip_code= models.CharField(max_length=10,blank=True)


    class Meta:
        verbose_name = ""  # Singular name
        verbose_name_plural = "User Profiles"  # Plural name (same as singular, to avoid pluralization)