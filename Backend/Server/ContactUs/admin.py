from django.contrib import admin
from .models import Contact


class ContactAdmin(admin.ModelAdmin):
    # Specify the fields to display in the list view
    list_display = ('full_name', 'email', 'phone')
    
    # Add filters to the right sidebar
    list_filter = ('email',)
    
    # Add search functionality
    search_fields = ('full_name', 'email', 'phone')
    
    # Specify the fields to be editable in the list view
    list_editable = ('phone',)
    
    # Customize the form layout
    fieldsets = (
        (None, {
            'fields': ('full_name', 'message')
        }),
        ('Contact Information', {
            'fields': ('phone', 'email')
        }),
    )
    
    # Optionally, you can set the ordering of the list view
    ordering = ('full_name',)

# Register your models here.
admin.site.register(Contact, ContactAdmin)