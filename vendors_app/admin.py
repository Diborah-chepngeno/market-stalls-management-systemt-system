from django.contrib import admin
from .models import Vendor, Stall, Payment

@admin.register(Vendor)
@admin.action(description='Approve selected vendors')
def approve_vendors(modeladmin, request, queryset):
    queryset.update(is_approved=True)

class VendorAdmin(admin.ModelAdmin):
    actions = [approve_vendors]
class VendorAdmin(admin.ModelAdmin):
    list_display = ('user', 'stall_number', 'contact_number', 'is_approved')
    list_filter = ('is_approved', 'registration_date')
    search_fields = ('user__username', 'stall_number')

@admin.register(Stall)
class StallAdmin(admin.ModelAdmin):
    list_display = ('number', 'location', 'size', 'is_occupied')
    ordering = ('number',)

@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ('vendor', 'amount', 'payment_date', 'status')
    date_hierarchy = 'payment_date'
    class PaymentInline(admin.TabularInline):  
    model = Payment
    extra = 1

class VendorAdmin(admin.ModelAdmin):
    inlines = [PaymentInline]
    
from django.contrib.admin import AdminSite

class MarketStallsAdminSite(AdminSite):
    site_header = "Market Stalls Administration"
    site_title = "Market Stalls Admin Portal"
    index_title = "Welcome to Market Stalls Admin"

market_stalls_admin = MarketStallsAdminSite(name='marketstallsadmin')

# Register models with custom admin site
market_stalls_admin.register(Vendor, VendorAdmin)
market_stalls_admin.register(Stall, StallAdmin)