from django.db import models

from applications.models.shared import BaseTimeModel

class EducationLevel(BaseTimeModel):
    level_name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.level_name