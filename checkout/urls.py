from django.urls import include, path
from .views import CheckoutView, PaymentCompletedView, PaymentFailedView 


app_name ="checkout"
urlpatterns = [
    path('', CheckoutView.as_view() ,name='checkout'),
    path('payment-completed/', PaymentCompletedView.as_view(), name='payment_completed'),
    path('payment-failed/', PaymentFailedView.as_view(), name='payment_failed'),
    path('paypal/',include('paypal.standard.ipn.urls'),name='paypal-ipn'),  # for paypal standard payment gateway
]