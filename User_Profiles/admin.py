from django.contrib import admin

# Register your models here.
from .models import User_Profiles



class User_Profiles_Admin(admin.ModelAdmin):
    list_display = ['user','phone','address_1','address_2','country','city','state','zip_code']

admin.site.register(User_Profiles,User_Profiles_Admin)


