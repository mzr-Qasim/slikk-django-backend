from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.


class Shoe_Packages_Plan(models.Model):
    plan_title = models.CharField(max_length=30,blank=True)
    plan_info = models.CharField(max_length=200,blank=True)
    plan_price = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(6)] , blank=True
    )
    plan_icon = models.CharField(max_length=60,blank=True)
        
    class Meta:
        verbose_name = ""  # Singular name
        verbose_name_plural = "Shoe Packages"  # Plural name (same as singular, to avoid pluralization)