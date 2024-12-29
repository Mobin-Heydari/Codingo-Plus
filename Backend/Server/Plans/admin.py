from django.contrib import admin
from .models import MainPlans, ServicePlan, PlanSupport, PlansFeature, PlanPrice

@admin.register(MainPlans)
class MainPlansAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'created', 'updated')  # Fields to display in the list view
    search_fields = ('name', 'slug')  # Fields to search in the admin interface
    prepopulated_fields = {'slug': ('name',)}  # Automatically populate the slug field from the name

@admin.register(ServicePlan)
class ServicePlanAdmin(admin.ModelAdmin):
    list_display = ('main_plan', 'sub_service')  # Fields to display in the list view
    search_fields = ('main_plan__name', 'sub_service__name')  # Search by main plan and sub-service names
    list_filter = ('main_plan',)  # Filter by main plan

@admin.register(PlanSupport)
class PlanSupportAdmin(admin.ModelAdmin):
    list_display = ('plan', 'free_support', 'supporting_price_per_month')  # Fields to display in the list view
    search_fields = ('plan__main_plan__name',)  # Search by the main plan name
    list_filter = ('plan',)  # Filter by service plan

@admin.register(PlansFeature)
class PlansFeatureAdmin(admin.ModelAdmin):
    list_display = ('plan', 'features', 'status')  # Fields to display in the list view
    search_fields = ('plan__main_plan__name', 'features__name')  # Search by main plan and feature names
    list_filter = ('plan', 'status')  # Filter by service plan and feature status

@admin.register(PlanPrice)
class PlanPriceAdmin(admin.ModelAdmin):
    list_display = ('plan', 'min_price', 'max_price', 'payment_steps')  # Fields to display in the list view
    search_fields = ('plan__main_plan__name',)  # Search by the main plan name
    list_filter = ('plan',)  # Filter by service plan
