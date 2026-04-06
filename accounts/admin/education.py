from django.contrib import admin

from ..models import Education


@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    list_display = ('user', 'university_name', 'degree', 'start_date', 'end_date')
    list_filter = ('university_name', 'degree', 'start_date', 'end_date')
    search_fields = ('university_name', 'degree', 'user__first_name', 'user__last_name')
    readonly_fields = ('created_at', 'updated_at')
    fieldsets = (
        ('User Information', {
            'fields': ('user',)
        }),
        ('Education Details', {
            'fields': ('university_name', 'degree')
        }),
        ('Duration', {
            'fields': ('start_date', 'end_date')
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )