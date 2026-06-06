from django.db import models
from django.conf import settings
from django.urls import reverse
from django.utils.text import slugify

from applications.models.shared import BaseTimeModel


def _post_image_upload_to(instance, filename):
    return f"posts/{instance.user.pk}/{filename}"


class Post(BaseTimeModel):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=300, unique=True, blank=True)
    description = models.TextField()
    image = models.ImageField(upload_to=_post_image_upload_to, null=True, blank=True)
    is_published = models.BooleanField(default=True)
    views = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ('-created_at',)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post_detail', args=[self.pk])

    def save(self, *args, **kwargs):
        if not self.slug:
            base = slugify(self.title)[:240]
            slug = base
            num = 1
            while Post.objects.filter(slug=slug).exclude(pk=self.pk).exists():
                slug = f"{base}-{num}"
                num += 1
            self.slug = slug
        super().save(*args, **kwargs)
