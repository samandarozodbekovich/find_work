from django.db import models

from applications.models.shared import BaseTimeModel
from .user import User

class Experience(BaseTimeModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='experience_set')
    company_name = models.CharField(max_length=255)
    position = models.CharField(max_length=255)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    description = models.TextField(blank=True, null=True)
    
    def __str__(self):
        return f"{self.position} at {self.company_name}"