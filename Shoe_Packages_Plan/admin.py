from django.contrib import admin

# Register your models here.
from Shoe_Packages_Plan.models import Shoe_Packages_Plan

class Shoe_Packages_Admin(admin.ModelAdmin):
    list_display = ['plan_title','plan_info','plan_price','plan_icon']

admin.site.register(Shoe_Packages_Plan,Shoe_Packages_Admin)