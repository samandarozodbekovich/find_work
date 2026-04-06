from django.db import models

from accounts.models.user import User
from applications.models.shared import BaseTimeModel
from .vacancy import Vacancy


class Application(BaseTimeModel):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    vacancy = models.ForeignKey(Vacancy, on_delete=models.SET_NULL, null=True, blank=True)
    status = models.CharField(max_length=20, default='pending')
    
    def __str__(self):
        return f"Application of {self.user.username} for {self.vacancy.title}"