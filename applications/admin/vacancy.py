from django.contrib import admin

from ..models import Vacancy


@admin.register(Vacancy)
class VacancyAdmin(admin.ModelAdmin):
    list_display = ('title', 'company', 'job_type', 'is_active', 'created_at')
    list_filter = ('is_active', 'company', 'job_type', 'experience_years', 'created_at')
    search_fields = ('title', 'description', 'company__company_name')
    readonly_fields = ('created_at', 'updated_at')
    fieldsets = (
        ('Company Information', {
            'fields': ('company',)
        }),
        ('Job Details', {
            'fields': (
                'title',
                'description',
                'job_type',
                'salary_min',
                'salary_max',
                'experience_years',
            )
        }),
        ('Status', {
            'fields': ('is_active',)
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )
