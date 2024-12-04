from django.contrib import admin
from django.contrib.auth.models import Group  # Import the Group model
from .models import User  # Import your User model



# Unregister the Group model
admin.site.unregister(Group)

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'user_type', 'joined_date', 'is_active')
    list_filter = ('user_type', 'is_active')
    search_fields = ('username', 'email')
    ordering = ('-joined_date',)
    
    fieldsets = (
        (None, {
            'fields': ('username', 'email', 'password')
        }),
        ('دسترسی', {
            'fields': ('is_active', 'is_staff', 'is_admin')
        }),
        ('نوع کاربری', {
            'fields': ('user_type',)
        }),
        ('اطلاعات تاریخ', {
            'fields': ('joined_date',),
            'classes': ('collapse',)
        }),
    )
    
    readonly_fields = ('joined_date',)