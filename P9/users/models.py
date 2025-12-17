"""
Models for CustomUser and UserFollows.
"""

from django.contrib.auth.models import AbstractUser
from django.db import models
from django.conf import settings


class CustomUser(AbstractUser):
    """Custom user model extending AbstractUser."""
    pass


class UserFollows(models.Model):
    """Model representing a user following another user."""
    user = models.ForeignKey(
        to=settings.AUTH_USER_MODEL,
        related_name="following",
        on_delete=models.CASCADE,
    )
    followed_user = models.ForeignKey(
        to=settings.AUTH_USER_MODEL,
        related_name="followed_by",
        on_delete=models.CASCADE,
    )

    class Meta:
        """Constraints for UserFollows model."""
        unique_together = ("user", "followed_user")

    def __str__(self):
        return f"{self.user} suit {self.followed_user}"
