from django.urls import path , include
from .views import HomeView,ScanView,SearchProductView


app_name ='product'
urlpatterns = [
    path('', HomeView.as_view(), name='home_view'),
    path('scan', ScanView.as_view(), name='scan_view'),
    path('search', SearchProductView.as_view(), name='search_product'),

    ]



