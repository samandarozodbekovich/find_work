from django.db import models

from applications.models.shared import BaseTimeModel
from .user import User

class Portfolio(BaseTimeModel):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    project_name = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField()
    link = models.URLField(blank=True, null=True)
    
    def __str__(self):
        return f"{self.project_name} - {self.user.first_name} {self.user.last_name}"