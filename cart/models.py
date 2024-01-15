# models.py
from django.db import models
from product.models import Product
from core.models import Customer


class Cart(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE , default=None, null=True)  # Many-to-one relationship with Customer
    created_at = models.DateTimeField(auto_now_add=True)
    total_price = models.DecimalField(max_digits=10, decimal_places=2, default=0)  # Total price can be calculated dynamically

    def __str__(self):
        return f"Cart for {self.customer.username}"


    def calculate_total_price(self):
        # Calculate total price dynamically based on associated CartItem instances
        cart_items = self.cartitem_set.all()  # Assuming the related name is 'cartitem_set'
        total_price = sum(item.item_price for item in cart_items)
        self.total_price = total_price
        self.save()
        return total_price



class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)  # Many-to-one relationship with Cart
    product = models.ForeignKey(Product, on_delete=models.CASCADE)  # Many-to-one relationship with Product
    quantity = models.PositiveIntegerField(default=1)
    unit_price = models.DecimalField(max_digits=10, decimal_places=2)
    item_price = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    def __str__(self):
        return f"{self.quantity} x {self.product.name} in {self.cart}"
    def save(self, *args, **kwargs):

        self.quantity = max(1, self.quantity)
        # If the product is Weight-based, restrict modification of quantity
        if self.product.category == Product.WEIGHT:
            self.quantity = 1

        # Calculate item price based on quantity
        self.item_price = self.product.price * self.quantity

        # Set unit_price if not already set (e.g., first save or if you want to persist the initial unit_price)
        # if not self.unit_price:
        #     self.unit_price = self.product.price
        super().save(*args, **kwargs)







