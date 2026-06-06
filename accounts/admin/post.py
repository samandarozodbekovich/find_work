from django.contrib import admin

from ..models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'user', 'is_published', 'created_at')
    list_filter = ('is_published', 'user')
    search_fields = ('title', 'description', 'user__username')
    readonly_fields = ('created_at', 'updated_at')
    prepopulated_fields = {'slug': ('title',)}
    fieldsets = (
        ('User', {'fields': ('user',)}),
        ('Content', {'fields': ('title', 'slug', 'description', 'image', 'is_published')}),
        ('Meta', {'fields': ('views', 'created_at', 'updated_at'), 'classes': ('collapse',)}),
    )
