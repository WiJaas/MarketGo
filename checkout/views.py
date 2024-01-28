from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.views import View
from django.views.generic import FormView

from django.urls import reverse
from django.conf import settings
from paypal.standard.forms import PayPalPaymentsForm
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseBadRequest


from .models import Order, OrderItem
from .forms import CheckoutForm
from cart.cart import Cart



app_name="checkout"

class CheckoutView(LoginRequiredMixin, FormView):
    template_name = 'checkout.html'
    form_class = CheckoutForm


    def get(self, request, *args, **kwargs):
        host = request.get_host()
        print(host)
        paypal_dict = {
            'business': settings.PAYPAL_RECEIVER_EMAIL,
            'amount': '200',
            'item_name': "Order_Item-No-7",
            'invoice': "INVOICE_NO-3",
            'currency_code': "MAD",
            'notify_url': 'http://{}{}'.format(host, reverse('paypal-ipn')),
            'return_url': 'http://{}{}'.format(host, reverse('checkout:payment_completed')),
            'cancel_url': 'http://{}{}'.format(host, reverse('checkout:payment_failed'))
        }


        form = PayPalPaymentsForm(initial=paypal_dict)
       
        return render(request, 'checkout.html',{'form':form} )




class PaymentCompletedView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'payment_completed.html')

class PaymentFailedView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'payment_failed.html')


# class PaymentView(View):

#     @csrf_exempt
#     def dispatch(self, *args, **kwargs):
#         return super().dispatch(*args, **kwargs)

#     def get(self, request, *args, **kwargs):
#         host = request.get_host()
#         paypal_dict = {
#             'business': settings.PAYPAL_RECEIVER_EMAIL,
#             'amount': '200',
#             'item_name': "Order_Item-No-3",
#             'invoice': "INVOICE_NO-3",
#             'currency_code': "MAD",
#             'notify_url': 'http://{}{}'.format(host, reverse("paypal-ipn")),
#             'return_url': 'http://{}{}'.format(host, reverse('checkout:paypal-completed')),
#             'cancel_url': 'http://{}{}'.format(host, reverse('checkout:paypal-failed'))
#         }


#         paypal_payment_button = PayPalPaymentsForm(initial=paypal_dict)
#         return render(request, 'checkout.html',{'paypal_payment_button':paypal_payment_button} )

#     def post(self, request, *args, **kwargs):
#         # Handle the post request if needed
#         return HttpResponseBadRequest("Bad Request")
