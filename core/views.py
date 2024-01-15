from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from . forms import SignUpForm
from .models import Customer 



class LoginView(View):
    template_name = 'login.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {})

    def post(self, request, *args, **kwargs):
        username = request.POST['username']
        password = request.POST['password']

        customer = authenticate(request, username=username, password=password)

        if customer is not None:
            login(request, customer)
            messages.success(request, ('You Have Been Logged In!'))
            return redirect('product:home_view')
        else:
            messages.error(request, ('Login failed. Please check your username and password.'))
            return render(request, self.template_name, {})

class LogoutView(View):
 def get(self, request, *args, **kwargs):
        logout(request)
        messages.success(request,"You have been logged out ... Thanks for Stopping By!")
        return redirect('core:login')


class RegisterView(View):
    template_name = 'register.html'
  
    def get(self, request, *args, **kwargs):
        form = SignUpForm()
        return render(request, self.template_name, {'form': form})
    
    def post(self, request, *args, **kwargs):
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            
            # log in user
            customer= authenticate(username=username, password=password)
            login(request, customer)
            messages.success(request, ("You Have Registered Successfully"))
            return redirect("product:home_view")
        else:
            messages.error(request, ("Whoops! There was a problem with your registration!"))
            return redirect('core:register')
