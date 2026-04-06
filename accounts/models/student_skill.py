from django.db import models

from accounts.models.user import User
from applications.models.shared import BaseTimeModel
from .skill import Skill


class StudentSkill(BaseTimeModel):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    skill = models.ForeignKey(Skill, on_delete=models.SET_NULL, null=True, blank=True)
    
    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name} - {self.skill.name}"