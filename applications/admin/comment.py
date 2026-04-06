from django.contrib import admin

from ..models import Comment


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['id', 'user__username', 'vacancy__title','body', 'is_active', 'created_at']
    list_filter = ['is_active', 'created_at']
    search_fields = ['user__username', 'vacancy__title', 'body']
    actions = ['disable_comments', 'active_comments']
    
    def disable_comments(self, request, queryset):
        queryset.update(is_active=False)
        
    def active_comments(self, request, queryset):
        queryset.update(is_active=True)