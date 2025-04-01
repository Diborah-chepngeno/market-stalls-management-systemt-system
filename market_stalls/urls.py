from django.contrib import Admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('vendors_app.urls')),
]
from django.urls import include, path

urlpatterns = [
    ...
    path('accounts/', include('accounts.urls')),
]