from django.db import models

from .user import User
from applications.models.shared import BaseTimeModel


class Education(BaseTimeModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='education_set')
    university_name = models.CharField(max_length=255)
    degree = models.CharField(max_length=100) 
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    
    def __str__(self):
        return f"{self.university_name} - {self.student.first_name}"