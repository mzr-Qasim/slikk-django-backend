from django.db import models

# Create your models here.


class Packages_Plan(models.Model): 
    category = models.CharField(max_length=30,blank=True)
    name = models.CharField(max_length=60,blank=True)
    plan_title = models.CharField(max_length=30,blank=True)
    plan_info = models.CharField(max_length=200,blank=True)
    price= models.DecimalField(max_digits=6, decimal_places=2, blank=True)
    image = models.FileField(upload_to='Package_Plans/')



    class Meta:
        verbose_name = ""  # Singular name
        verbose_name_plural = "Packages Plan"  # Plural name (same as singular, to avoid pluralization)