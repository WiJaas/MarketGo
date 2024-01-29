from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.views.generic import DetailView
from django.views.generic import FormView
from product.models import Product
from .models import Order, OrderItem
from .forms import CheckoutForm
from cart.cart import Cart
from django.urls import reverse


class CheckoutView(LoginRequiredMixin, FormView):
    template_name = 'checkout.html'
    form_class = CheckoutForm

    def form_valid(self, form, *args, **kwargs):
        cart = Cart(self.request)
        if not cart.cart:  # If the cart is empty, redirect to the cart page
            return redirect('cart:cart_detail')
    #   Calculate total price 

  
        order = form.save(commit=False)
        order.user = self.request.user

        # Save total amount in DB 


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
        

        print(order)
        print(order.paid_amount)



        
        # Optionally, you can clear the cart after placing the order
        cart.clear()


        # return HttpResponse('Order placed successfully!')
        return redirect(reverse('checkout:invoice', kwargs={'pk': order.id}))




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
    





class InvoiceDetailView(DetailView):
    template_name = 'invoice.html'
    context_object_name = 'order'  # This sets the variable name in the template
    model = Order  # This sets the model for the view

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        order = context['order']

        # Add related OrderItem instances to the context
        context['order_items'] = OrderItem.objects.filter(order=order)
        print(context)
        return context