from django.urls import path
from .views import CartAddView, CartDetailView, CartRemoveView,CartUpdateQuantityView

app_name = 'cart'

urlpatterns = [
    path('', CartDetailView.as_view(), name='cart_detail'),
    path('add/<int:product_id>/', CartAddView.as_view(), name='cart_add'),
     path('update_quantity/<int:product_id>/', CartUpdateQuantityView.as_view(), name='update_quantity'),
    path('remove/<int:product_id>/', CartRemoveView.as_view(), name='cart_remove'),

]