from django.contrib import admin
from .models import User  # Import your User model

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'user_type', 'joined_date', 'is_active')  # Display these fields in the list view
    list_filter = ('user_type', 'is_active')  # Add filters for user type and active status
    
    search_fields = ('username', 'email')  # Enable search by username and email
    
    ordering = ('-joined_date',)  # Order users by joined date descending
    
    fieldsets = (
        (None, {
            'fields': ('username', 'email', 'password')
        }),
        ('Permissions', {
            'fields': ('is_active', 'is_staff', 'is_admin')
        }),
        ('User  Type', {
            'fields': ('user_type',)
        }),
        ('Date  Information', {
            'fields': ('joined_date',),
            'classes': ('collapse',)  # Makes this section collapsible
        }),
    )
    
    readonly_fields = ('joined_date',)  # Make the joined date read-only
