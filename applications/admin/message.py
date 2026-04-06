from django.contrib import admin

from ..models import Message


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('sender', 'application', 'is_read', 'created_at')
    list_filter = ('is_read', 'created_at', 'sender')
    search_fields = ('sender__username', 'sender__email', 'content', 'application__vacancy__title')
    readonly_fields = ('created_at', 'updated_at')
    fieldsets = (
        ('Message Information', {
            'fields': ('application', 'sender')
        }),
        ('Content', {
            'fields': ('content',)
        }),
        ('Status', {
            'fields': ('is_read',)
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )
