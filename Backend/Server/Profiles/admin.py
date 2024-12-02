from django.contrib import admin
from .models import CustomersProfile, EmployeeProfile, EmployeeSkils # Import your profile models

class CustomersProfileAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'customer', 'bio')  # Display these fields in the list view
    search_fields = ('full_name', 'customer__username')  # Enable search by full name and customer username
    list_filter = ('customer__user_type',)  # Filter by customer user type

class EmployeeProfileAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'employee', 'job_title', 'years_of_experience')  # Display these fields in the list view
    search_fields = ('full_name', 'employee__username')  # Enable search by full name and employee username
    list_filter = ('employee__user_type', 'employee_stack')  # Filter by employee user type and stack

admin.site.register(CustomersProfile, CustomersProfileAdmin)
admin.site.register(EmployeeProfile, EmployeeProfileAdmin)

admin.site.register(EmployeeSkils)