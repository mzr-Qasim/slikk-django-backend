from django.contrib import admin

# Register your models here.
from .models import Site_Settings



class Site_Settings_Admin(admin.ModelAdmin):
    list_display = ['GST','logo']

admin.site.register(Site_Settings,Site_Settings_Admin)