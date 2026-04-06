from django.contrib.auth.models import AbstractUser
from django.db import models

from applications.models.shared import BaseTimeModel

class User(AbstractUser, BaseTimeModel):
    ROLE_CHOICES = (('student', 'Student'), ('employer', 'Employer'))
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='student')
    
    resume_url = models.FileField(upload_to='resumes/', null=True, blank=True)
    education_level = models.ForeignKey('EducationLevel', on_delete=models.SET_NULL, null=True, blank=True)
    bio = models.TextField(blank=True, null=True)
    
    def __str__(self):
        return self.username