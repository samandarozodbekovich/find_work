from django.db import models

from applications.models.shared import BaseTimeModel
from .user import User

class Certificate(BaseTimeModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=255)
    files = models.FileField(upload_to='certificates/', blank=True, null=True)
    link = models.URLField(blank=True, null=True)
    issue_date = models.DateField(blank=True, null=True)