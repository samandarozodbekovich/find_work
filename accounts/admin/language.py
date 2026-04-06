from django.contrib import admin

from ..models import Language, LanguageLevel


@admin.register(Language)
class LanguageAdmin(admin.ModelAdmin):
    list_display = ["id","name"]
    
    
@admin.register(LanguageLevel)
class LanguageLevelAdmin(admin.ModelAdmin):
    list_display = ["id","level_name"]