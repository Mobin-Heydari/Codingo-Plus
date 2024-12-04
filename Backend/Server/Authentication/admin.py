from django.contrib import admin
from .models import OneTimePassword

class OneTimePasswordAdmin(admin.ModelAdmin):
    # Specify the fields to display in the list view
    list_display = ('email', 'code', 'token', 'status', 'expiration', 'created')
    
    # Add filters to the right sidebar
    list_filter = ('status',)
    
    # Add search functionality
    search_fields = ('email', 'code', 'token')
    
    # Customize the form layout
    fieldsets = (
        (None, {
            'fields': ('email', 'code', 'token')
        }),
        ('Status and Timing', {
            'fields': ('status', 'expiration')
        }),
    )
    
    ordering = ['-created']

# Register your models here.
admin.site.register(OneTimePassword, OneTimePasswordAdmin)