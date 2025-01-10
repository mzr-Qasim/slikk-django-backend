from django.contrib import admin

# Register your models here.
from .models import Packages_Plan



class Laundary_Packages_Admin(admin.ModelAdmin):
    list_display = ['category','plan_title','plan_info','plan_price','plan_icon']

admin.site.register(Packages_Plan,Laundary_Packages_Admin)