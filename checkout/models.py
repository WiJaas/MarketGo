# Create your models here.
from django.db import models
from django.contrib.auth.models import User
from product.models import Product

class Order(models.Model):
    ONLINE = 'Online'
    CASH = 'Cash'

    PAYMENT_CHOICES = (
        (ONLINE, 'Online'),
        (CASH, 'Cash')
    )

    user = models.ForeignKey(User, related_name='orders', blank=True, null=True, on_delete=models.CASCADE)
    
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    
    created_at = models.DateTimeField(auto_now_add=True)

    paid = models.BooleanField(default=False)
    paid_amount = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)

    payment_method = models.CharField(max_length=20, choices=PAYMENT_CHOICES, default=ONLINE)

    def __str__(self):
        return f"Order #{self.id} - {self.first_name} {self.last_name}"

class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name='items', on_delete=models.CASCADE)
    price = models.FloatField()
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return f"{self.quantity} x {self.product.name} in Order #{self.order.id}"
