from django.db import models

from applications.models.shared import BaseTimeModel

class Skill(BaseTimeModel):
    name = models.CharField(max_length=100, unique=True)
    is_custom = models.BooleanField(default=False)
    
    def __str__(self):
        return self.name