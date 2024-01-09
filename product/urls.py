from django.urls import path , include
from . import views

urlpatterns = [
    path('', views.home_view),
    # path('search/', views.scan_barcode, name='search_product'),
    # New URL pattern for search_by_scan
    # path('search_by_scan/', views.search_by_scan, name='search_by_scan'),
    path('scan_view/', views.scan_view, name='scan_view'),
    path('search_product/', views.search_product, name='search_product'),
    
    # path('redirect_to_search/<str:barcode>/', redirect_to_search, name='redirect_to_search'),


    ]



