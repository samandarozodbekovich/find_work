from django.db import models

from applications.models.shared import BaseTimeModel
from .company import Company

class Vacancy(BaseTimeModel):
    company = models.ForeignKey(Company, on_delete=models.SET_NULL, null=True, blank=True)
    title = models.CharField(max_length=255)
    description = models.TextField()
    is_active = models.BooleanField(default=True)
    
    # New fields for filtering
    job_type = models.CharField(
        max_length=50,
        choices=[
            ('full_time', 'To\'liq stavka'),
            ('part_time', 'Yarim stavka'),
            ('contract', 'Kontrakt'),
            ('freelance', 'Frilans'),
            ('internship', 'Stajirovka'),
        ],
        blank=True,
        null=True
    )
    salary_min = models.IntegerField(blank=True, null=True)
    salary_max = models.IntegerField(blank=True, null=True)
    experience_years = models.IntegerField(
        choices=[
            (0, 'Tajribasiz'),
            (1, '1 yil'),
            (2, '2 yil'),
            (3, '3 yil'),
            (5, '5 yil'),
            (10, '10+ yil'),
        ],
        blank=True,
        null=True
    )
    
    @property
    def region(self):
        if self.company and self.company.city:
            return self.company.city.region
        return None
    
    def __str__(self):
        return f"{self.title} at {self.company.company_name}"