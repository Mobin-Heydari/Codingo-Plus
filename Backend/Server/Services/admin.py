from django.contrib import admin
from .models import MainServices, SubService, Feature

# Register the MainServices model
@admin.register(MainServices)
class MainServicesAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'image')  # Fields to display in the list view
    search_fields = ('name', 'slug')  # Fields to search in the admin interface

# Register the SubService model
@admin.register(SubService)
class SubServiceAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'image', 'icon')  # Fields to display in the list view
    search_fields = ('name', 'slug')  # Fields to search in the admin interface

# Register the Feature model
@admin.register(Feature)
class FeatureAdmin(admin.ModelAdmin):
    list_display = ('title', 'sub_service', 'icon')  # Fields to display in the list view
    search_fields = ('title',)  # Fields to search in the admin interface