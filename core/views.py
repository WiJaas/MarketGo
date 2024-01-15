from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from . forms import SignUpForm
from django.contrib.auth.models import User



class LoginView(View):
    template_name = 'login.html'
    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {})
    def post(self, request, *args, **kwargs):
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, ("You Have Been Logged In!"))
            print(username)
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
            print(username)
            print(password)
            # log in user
            user= authenticate(username=username, password=password)
            print(user)
            login(request, user)
            messages.success(request, ("You Have Registered Successfully"))
            return redirect("product:home_view")
        else:
            messages.success(request, ("Whoops! There was a problem Registering, please try again..."))
            return redirect('core:register')


