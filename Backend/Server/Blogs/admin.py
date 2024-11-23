from django.contrib import admin
from . import models

class SectionsInline(admin.TabularInline):
    model = models.BlogSection
    extra = 1  # Number of empty forms to display
    verbose_name = "Blog Section"
    verbose_name_plural = "Blog Sections"

@admin.register(models.Blog)
class BlogAdmin(admin.ModelAdmin):
    inlines = [SectionsInline]
    list_display = ['title', 'slug', 'created', 'updated']
    list_filter = ['created', 'updated']
    search_fields = ['title', 'slug']
    ordering = ['-created']  # Order by creation date descending
    fieldsets = (
        (None, {
            'fields': ('title', 'slug', 'content')
        }),
        ('Meta Information', {
            'fields': ('created', 'updated'),
            'classes': ('collapse',)  # Makes this section collapsible
        }),
    )
    readonly_fields = ('created', 'updated')

    def save_model(self, request, obj, form, change):
        if not change:  # If the object is new, set created_at
            obj.created_at = timezone.now()
        super().save_model(request, obj, form, change)
