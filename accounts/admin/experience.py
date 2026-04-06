from django.contrib import admin

from ..models import Experience


@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display = ('position', 'company_name', 'user', 'start_date', 'end_date')
    list_filter = ('start_date', 'end_date', 'company_name')
    search_fields = ('position', 'company_name', 'user__first_name', 'user__last_name')
    readonly_fields = ('created_at', 'updated_at')
    fieldsets = (
        ('User Information', {
            'fields': ('student',)
        }),
        ('Experience Details', {
            'fields': ('company_name', 'position', 'description')
        }),
        ('Duration', {
            'fields': ('start_date', 'end_date')
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )
