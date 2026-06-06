from django.db import models

from accounts.models.user import User
from applications.models.shared import BaseTimeModel
from .vacancy import Vacancy


class Application(BaseTimeModel):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('accepted', 'Accepted'),
        ('rejected', 'Rejected'),
    ]
    
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    vacancy = models.ForeignKey(Vacancy, on_delete=models.SET_NULL, null=True, blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    
    def __str__(self):
        user = self.user.username if self.user else 'Deleted User'
        vacancy = self.vacancy.title if self.vacancy else 'Deleted Vacancy'
        return f"Application of {user} for {vacancy}"