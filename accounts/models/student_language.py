from django.db import models

from applications.models.shared import BaseTimeModel
from .language import Language, LanguageLevel
from .user import User


class StudentLanguage(BaseTimeModel):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    language = models.ForeignKey(Language, on_delete=models.SET_NULL, null=True, blank=True)
    level = models.ForeignKey(LanguageLevel, on_delete=models.SET_NULL, null=True, blank=True)
    
    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name} - {self.language.name} ({self.level.level_name})"