from django.contrib import admin

from ..models import Vacancy


@admin.register(Vacancy)
class VacancyAdmin(admin.ModelAdmin):
    list_display = ('title', 'company', 'salary_range', 'is_active', 'created_at')
    list_filter = ('is_active', 'company', 'created_at')
    search_fields = ('title', 'description', 'company__company_name')
    readonly_fields = ('created_at', 'updated_at')
    fieldsets = (
        ('Company Information', {
            'fields': ('company',)
        }),
        ('Job Details', {
            'fields': ('title', 'description', 'salary_range')
        }),
        ('Status', {
            'fields': ('is_active',)
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )
