from django.db import models

from accounts.models.user import User
from .application import Application
from applications.models.shared import BaseTimeModel

class Message(BaseTimeModel):
    application = models.ForeignKey(Application, on_delete=models.SET_NULL, null=True, blank=True)
    sender = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    content = models.TextField()
    is_read = models.BooleanField(default=False)
    
    def __str__(self):
        return f"Message from {self.sender.username} regarding {self.application.vacancy.title}"
