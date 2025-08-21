from django.contrib.auth.models import AbstractUser
from django.db import models
from django.conf import settings


class User(AbstractUser):

    def __str__(self):
        return f"{self.username}: ({self.first_name} {self.last_name})"


class Profile(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        related_name="profile",
        on_delete=models.CASCADE
    )
    bio = models.TextField(
        max_length=512,
        null=True,
        blank=True
    )
    avatar = models.ImageField(
        null=True, blank=True, upload_to="accounts/profiles/avatars/"
    )
    phone = models.CharField(max_length=20, null=True, blank=True)
    city = models.CharField(max_length=63, null=True, blank=True)
    country = models.CharField(max_length=32, null=True, blank=True)
    is_public = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)


    class Meta:
        verbose_name = "Profile"
        verbose_name_plural = "Profiles"
        ordering = ["-created_at"]

    def __str__(self):
        return f"Profile: {self.user.username}"
