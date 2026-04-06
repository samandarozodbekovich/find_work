from django.contrib import admin

from ..models import StudentLanguage


@admin.register(StudentLanguage)
class StudentLanguageAdmin(admin.ModelAdmin):
    list_display = ('user', 'language', 'level')
    list_filter = ('language', 'level')
    search_fields = ('user__first_name', 'user__last_name', 'language__name')
    readonly_fields = ('created_at', 'updated_at')
    fieldsets = (
        ('User Information', {
            'fields': ('user',)
        }),
        ('Language Details', {
            'fields': ('language', 'level')
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )
