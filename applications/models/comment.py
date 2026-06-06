from django.db import models
from django.conf import settings

from .vacancy import Vacancy

from .shared import BaseTimeModel
from accounts.models.post import Post


class Comment(BaseTimeModel):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, blank=True, null=True, related_name="comments")
    vacancy = models.ForeignKey(Vacancy, on_delete=models.SET_NULL, blank=True, null=True, related_name="comments")
    post = models.ForeignKey(Post, on_delete=models.SET_NULL, blank=True, null=True, related_name="comments")
    body = models.TextField()
    is_active = models.BooleanField(default=True)
    
    class Meta:
        ordering = ["-created_at"]
    
    def __str__(self):
        return f"{self.user.username} commented {self.vacancy.title}"
    
    