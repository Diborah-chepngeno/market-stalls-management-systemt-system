from django.contrib.auth import login, logout
from django.shortcuts import render, redirect
from .forms import LoginForm, RegisterForm

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('dashboard')
    else:
        form = LoginForm()
    return render(request, 'accounts/login.html', {'form': form})

def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('dashboard')
    else:
        form = RegisterForm()
    return render(request, 'accounts/register.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('home')
from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.views.decorators.csrf import csrf_protect

@csrf_protect
def login_view(request):
    if request.method == 'POST':
        # ... authentication logic ...
        if user is not_valid:
            # Track failed attempts
            request.session['login_attempts'] = request.session.get('login_attempts', 0) + 1
            return render(request, 'accounts/login.html', {'error': 'Invalid credentials'})
        
        # Successful login
        login(request, user)
        request.session['last_login'] = str(timezone.now())
        request.session['user_type'] = 'vendor'  # Custom session data
        request.session.set_expiry(1209600)  # Override global session age
        return redirect('dashboard')