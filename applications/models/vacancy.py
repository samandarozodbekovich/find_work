from django.db import models

from applications.models.shared import BaseTimeModel
from .company import Company

class Vacancy(BaseTimeModel):
    company = models.ForeignKey(Company, on_delete=models.SET_NULL, null=True, blank=True)
    title = models.CharField(max_length=255)
    description = models.TextField()
    salary_range = models.CharField(max_length=50)
    is_active = models.BooleanField(default=True)
    
    def __str__(self):
        return f"{self.title} at {self.company.company_name}"