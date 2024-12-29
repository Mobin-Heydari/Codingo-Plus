from django.contrib import admin
from .models import Project

class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'status', 'created_at', 'updated_at')
    list_filter = ('status', 'created_at')
    search_fields = ('title', 'description')
    ordering = ('created_at',)
    date_hierarchy = 'created_at'
    prepopulated_fields = {'slug': ('title',)}  # If you have a slug field

admin.site.register(Project, ProjectAdmin)