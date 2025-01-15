from django.contrib import admin

# Register your models here.

from .models import Order, OrderPackages



class Order_Admin(admin.ModelAdmin):
    list_display = ['user', 'created_at', 'updated_at', 'status','payment_status', 'payment_id', 'total_price']

admin.site.register(Order,Order_Admin)