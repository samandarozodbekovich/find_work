from django.db import models

from applications.models.shared import BaseTimeModel


class Language(BaseTimeModel):
    name = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name
    

class LanguageLevel(BaseTimeModel):
    level_name = models.CharField(max_length=10)
    
    def __str__(self):
        return self.level_name
    
    
