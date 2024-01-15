
from django.db import models

class Product(models.Model):
    UNIT = 'unit'
    WEIGHT = 'weight'
    CATEGORY_CHOICES = [
        (UNIT, 'Unit'),
        (WEIGHT, 'Weight'),
    ]
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2) # price per item
    category = models.CharField(max_length=10, choices=CATEGORY_CHOICES) # Unit-Based or Weight-Based 
    barcode = models.CharField(max_length=13, unique=True)
    stock_quantity = models.PositiveIntegerField(default=0) # Only for Unit-Based Items
    weight = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    image = models.ImageField(upload_to='product_images/', blank=True, null=True)


    def __str__(self):
        if self.category == self.WEIGHT:
            return f"{self.name} ({self.category}) - ${self.price:.2f} - {self.description[:50]}... - Barcode: {self.barcode} - Weight: {self.weight} kg"
        else:
            return f"{self.name} ({self.category}) - ${self.price:.2f} - {self.description[:50]}... - Barcode: {self.barcode} - Stock Quantity: {self.stock_quantity}"
        
    def reduce_stock(self, quantity):
        if self.stock_quantity >= quantity:
            self.stock_quantity -= quantity
            self.save()
            return True
        return False