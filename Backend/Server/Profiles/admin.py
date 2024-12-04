from django.contrib import admin
from .models import SimpleUserProfile, EmployeeProfile, EmployeeSkills

class EmployeeSkillsInline(admin.TabularInline):
    model = EmployeeSkills
    extra = 1  # Number of empty forms to display
    verbose_name = "Employee Skill"
    verbose_name_plural = "Employee Skills"

class SimpleUserProfileAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'user__username', 'bio')
    search_fields = ('full_name', 'user__username')

class EmployeeProfileAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'employee', 'job_title', 'years_of_experience')
    search_fields = ('full_name', 'employee__username', 'job_title')
    list_filter = ('employee__user_type', 'employee__user_type')
    ordering = ('-years_of_experience',)
    inlines = [EmployeeSkillsInline]  # Include the inline class here

# Register your models with the customized admin classes
admin.site.register(SimpleUserProfile, SimpleUserProfileAdmin)
admin.site.register(EmployeeProfile, EmployeeProfileAdmin)