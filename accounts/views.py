from django.shortcuts import render,redirect,get_object_or_404
from django.contrib import messages

# Create your views here.
from .forms import  SignUpForm 
from django.contrib.auth.models import User 
from django.contrib.auth.decorators import login_required

from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.http import JsonResponse

from .models import Profile

# Create your views here.


def register_user(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            # Log in user
            user = authenticate(username=username, password=password)
            login(request,user)
            messages.success(request, ("You have successfully registered! Welcome!"))
            return redirect('home')
        else:
            errors = form.errors
            for field, error_list in errors.items():
                for error in error_list:
                        messages.error(request, f"{error}")

    form = SignUpForm()
    return render(request, 'accounts/register.html', {"form":form})


def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user  = authenticate(request,username=username,password=password)
    
        if user is not None:
            login(request,user)
            messages.success(request,("Login successful"))
            return redirect('home')
        
        messages.success(request,("Invalid username or password Try again"))
        return redirect('login')

    return render(request, 'accounts/login.html')


def logout_user(request):
    logout(request)
    messages.success(request,("logout of successful"))
    return redirect('login')


def update_profile(request):
    current_user = User.objects.get(id=request.user.id)

    profile = Profile.objects.get(user=current_user)

    if request.method == 'POST':
        profile.is_seller = True
        profile.save()

        login(request, current_user)
        messages.success(request, ("Your Profile Has Been Updated!"))
        return redirect('home')

    return render(request, "accounts/update_user.html")


def home(request):

    if request.user.is_authenticated:
        try:
            profile = Profile.objects.get(user= request.user)
        except Profile.DoesNotExist:
            profiles = None
        
        context = {
        "profile" :profile
        }

        return render(request, 'home.html',context)

    return render(request, 'home.html')



