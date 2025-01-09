from django.db import models

# Create your models here.
class Packages_Section(models.Model): 
    first_section_title = models.CharField(max_length=50,blank=True)
    first_section_info = models.CharField(max_length=200,blank=True)
    second_section_title = models.CharField(max_length=50,blank=True)
    second_section_info = models.CharField(max_length=200,blank=True)


    class Meta:
        verbose_name = ""  # Singular name
        verbose_name_plural = "Packages Section"  # Plural name (same as singular, to avoid pluralization)