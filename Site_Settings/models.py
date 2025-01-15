from django.db import models

# Create your models here.
class Site_Settings(models.Model): 
    GST= models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    logo = models.FileField(upload_to='Site_Logo/')


    class Meta:
        verbose_name = ""  # Singular name
        verbose_name_plural = "Site Settings"  # Plural name (same as singular, to avoid pluralization)