from django.contrib import admin

from ..models import Application


@admin.register(Application)
class ApplicationAdmin(admin.ModelAdmin):
    list_display = ('user', 'vacancy', 'status', 'created_at')
    list_filter = ('status', 'created_at', 'vacancy')
    search_fields = ('user__first_name', 'user__last_name', 'vacancy__title', 'vacancy__company__name')
    readonly_fields = ('created_at', 'updated_at')
    fieldsets = (
        ('Applicant Information', {
            'fields': ('user',)
        }),
        ('Job Vacancy', {
            'fields': ('vacancy',)
        }),
        ('Application Status', {
            'fields': ('status',)
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )
