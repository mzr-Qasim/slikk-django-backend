from django.contrib import admin

# Register your models here.
from .models import Site_Logo



class Site_Logo_Admin(admin.ModelAdmin):
    list_display = ['logo']

admin.site.register(Site_Logo,Site_Logo_Admin)