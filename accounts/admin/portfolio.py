from django.contrib import admin

from ..models import Portfolio


@admin.register(Portfolio)
class PortfolioAdmin(admin.ModelAdmin):
    list_display = ('project_name', 'user', 'link')
    list_filter = ('project_name', 'user')
    search_fields = ('project_name', 'description', 'user__first_name', 'user__last_name')
    readonly_fields = ('created_at', 'updated_at')
    fieldsets = (
        ('User Information', {
            'fields': ('user',)
        }),
        ('Portfolio Details', {
            'fields': ('project_name', 'link', 'description')
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )