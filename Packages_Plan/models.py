from django.db import models

# Create your models here.


class Laundary_Packages(models.Model): 
    plan_title = models.CharField(max_length=30,blank=True)
    plan_info = models.CharField(max_length=200,blank=True)
    plan_price= models.DecimalField(max_digits=6, decimal_places=2, blank=True)
    plan_icon = models.CharField(max_length=60,blank=True)


    class Meta:
        verbose_name = ""  # Singular name
        verbose_name_plural = "Laundary Packages"  # Plural name (same as singular, to avoid pluralization)