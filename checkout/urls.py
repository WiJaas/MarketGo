from django.urls import path
from .views import CheckoutView,InvoiceDetailView


app_name ="checkout"
urlpatterns = [
    path('', CheckoutView.as_view(), name='checkout'),
    path('invoice/<int:pk>/', InvoiceDetailView.as_view(), name='invoice'),
    path('dashboard/', DashboardView.as_view(), name='dashboard'),


]