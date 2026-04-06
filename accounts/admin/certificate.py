from django.contrib import admin

from ..models import Certificate

@admin.register(Certificate)
class CertificateAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'title']
    list_filter = ["user", "issue_date", "created_at"]
    search_fields = ["user", "title"]
    
    