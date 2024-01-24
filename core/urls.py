from django.urls import path
from .views import LoginView, LogoutView, RegisterView , MyAccountView

app_name = 'core'

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', RegisterView.as_view(), name='register'),
    path('myaccount/',MyAccountView.as_view() , name='myaccount'),


    # other URL patterns for your app
]
