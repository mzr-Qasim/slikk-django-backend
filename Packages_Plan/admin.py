from django.contrib import admin

# Register your models here.
from .models import Packages_Plan



class Laundary_Packages_Admin(admin.ModelAdmin):
    list_display = ['category','name', 'plan_title','plan_info','price','image','GST']

admin.site.register(Packages_Plan,Laundary_Packages_Admin)