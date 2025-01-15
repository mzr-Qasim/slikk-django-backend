from django.db import models

# Create your models here.
class Site_Logo(models.Model): 
    logo = models.FileField(upload_to='Site_Logo/')


    class Meta:
        verbose_name = ""  # Singular name
        verbose_name_plural = "Site Logo"  # Plural name (same as singular, to avoid pluralization)