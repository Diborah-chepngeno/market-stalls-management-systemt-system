# admin.py
from django.contrib.sessions.models import Session
from django.contrib import admin

class SessionAdmin(admin.ModelAdmin):
    list_display = ['session_key', 'expire_date']
    search_fields = ['session_key']
    
admin.site.register(Session, SessionAdmin)