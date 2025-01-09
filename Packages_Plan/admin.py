from django.contrib import admin

# Register your models here.
from .models import Laundary_Packages



class Laundary_Packages_Admin(admin.ModelAdmin):
    list_display = ['plan_title','plan_info','plan_price','plan_icon']

admin.site.register(Laundary_Packages,Laundary_Packages_Admin)