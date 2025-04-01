from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('dashboard/', views.dashboard_view, name='dashboard'),
]
# backend/vendors_app/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_view, name='login'),
    # other app URLs...
]

# backend/market_stalls/urls.py (main project)
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('vendors_app.urls')),
]
from django.urls import path
from .admin import market_stalls_admin

urlpatterns = [
    path('admin/', market_stalls_admin.urls),
]