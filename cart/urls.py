from django.urls import path
from . import views


urlpatterns = [
    path('', views.cart_view, name="cart_view"),
    path('add/', views.cart_view, name="cart_add"),
    path('delete/', views.cart_view, name="cart_delete"),
    path('update/', views.cart_view, name="cart_update"),
]