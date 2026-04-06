from django.contrib import admin

from ..models import StudentSkill


@admin.register(StudentSkill)
class StudentSkillAdmin(admin.ModelAdmin):
    list_display = ('user', 'skill')
    list_filter = ('skill',)
    search_fields = ('user__first_name', 'user__last_name', 'skill__name')
    readonly_fields = ('created_at', 'updated_at')
    fieldsets = (
        ('Student Information', {
            'fields': ('student',)
        }),
        ('Skill Details', {
            'fields': ('skill',)
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )
