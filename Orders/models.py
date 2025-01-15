from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Order(models.Model):
    user= models.ForeignKey(User, on_delete=models.CASCADE, related_name='orders')
    created_at= models.DateTimeField(auto_now_add=True)
    updated_at= models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, default='Pending')
    payment_status = models.CharField(max_length=20, default='Unpaid')
    payment_id = models.CharField(max_length=20, null=True)
    total_price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)

    def __str__(self):
        return f"Orders {self.id} by {self.user.username}"


class OrderPackages(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='packages')
    package_name= models.CharField(max_length=255)
    quantity= models.IntegerField(default=1)
    price = models.DecimalField(max_digits=10, decimal_places=2)


    def __str__(self):
        return f"{self.quantity} x {self.package_name} (Order{self.order.id})"
    
    
    def get_total_package_price(self):
        return self.quantity * self.price