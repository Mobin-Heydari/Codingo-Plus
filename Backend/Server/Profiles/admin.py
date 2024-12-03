from django.contrib import admin
from .models import SimpleUserProfile, EmployeeProfile, EmployeeSkils # Import your profile models

class SimpleUserProfileAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'user', 'bio')  # Display these fields in the list view
    search_fields = ('full_name', 'user__username')  # Enable search by full name and user username
    list_filter = ('user__user_type',)  # Filter by user user type

class EmployeeProfileAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'employee', 'job_title', 'years_of_experience')  # Display these fields in the list view
    search_fields = ('full_name', 'employee__username')  # Enable search by full name and employee username
    list_filter = ('employee__user_type', 'employee_stack')  # Filter by employee user type and stack

admin.site.register(SimpleUserProfile, SimpleUserProfileAdmin)
admin.site.register(EmployeeProfile, EmployeeProfileAdmin)

admin.site.register(EmployeeSkils)