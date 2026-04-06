from django.db import models

from applications.models.shared import BaseTimeModel

class City(BaseTimeModel):
    name = models.CharField(max_length=100)
    region = models.CharField(max_length=100)
    
    def __str__(self):
        return f"{self.name}, {self.region}"