from django.shortcuts import render

def register_view(request):
    return render(request, 'register/index.html')

def login_view(request):
    return render(request, 'login/index.html')

def dashboard_view(request):
    return render(request, 'dashboard/index.html')
from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login
from .forms import VendorRegistrationForm
from django.contrib.auth.models import User
from .models import Vendor

def register_view(request):
    if request.method == 'POST':
        form = VendorRegistrationForm(request.POST)
        if form.is_valid():
            # Create user
            user = User.objects.create_user(
                username=form.cleaned_data['username'],
                email=form.cleaned_data['email'],
                password=form.cleaned_data['password1']
            )
            
            # Create vendor
            Vendor.objects.create(
                user=user,
                stall_number=form.cleaned_data['stall_number'],
                contact_number=form.cleaned_data['contact_number']
            )
            
            # Log the user in
            auth_login(request, user)
            return redirect('dashboard')
    else:
        form = VendorRegistrationForm()
    
    return render(request, 'register/index.html', {'form': form})
# backend/vendors_app/views.py
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            return render(request, 'login/index.html', {'error': 'Invalid credentials'})
    
    return render(request, 'login/index.html')