from django.contrib import admin

from ..models import EducationLevel


@admin.register(EducationLevel)
class EducationLevelAdmin(admin.ModelAdmin):
    list_display = ['level_name', 'created_at']
    