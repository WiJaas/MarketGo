from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.views.generic import FormView

from product.models import Product
from .models import Order, OrderItem
from .forms import CheckoutForm
from cart.cart import Cart

class CheckoutView(LoginRequiredMixin, FormView):
    template_name = 'checkout.html'
    form_class = CheckoutForm

    def form_valid(self, form, *args, **kwargs):
        cart = Cart(self.request)
        if not cart.cart:  # If the cart is empty, redirect to the cart page
            return redirect('cart:cart_detail')

        order = form.save(commit=False)
        order.user = self.request.user
        order.save()

        # Create OrderItems for each item in the cart
        for item in cart:
          
            product = item['product']
            order_item=OrderItem.objects.create(
                order=order,
                product=product,
                price=item['price'],
                quantity=item['quantity'],
            )
        print(order_item)



        # Optionally, you can clear the cart after placing the order
        cart.clear()

        return HttpResponse('Order placed successfully!')



    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form, *args, **kwargs)
        else:
            print(form.errors)
            return self.form_invalid(form, *args, **kwargs)

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['cart'] = Cart(self.request)
        return context
