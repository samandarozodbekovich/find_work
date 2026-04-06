from django.db import models

from accounts.models.user import User
from applications.models.shared import BaseTimeModel
from .city import City

class Company(BaseTimeModel):
    user = models.OneToOneField(User, on_delete=models.SET_NULL, null=True, blank=True)
    company_name = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    city = models.ForeignKey(City, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.company_name