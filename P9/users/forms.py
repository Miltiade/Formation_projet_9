"""
Forms for CustomUser and UserFollows.
"""

from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser
from django import forms


class CustomUserCreationForm(UserCreationForm):
    """Form for creating a new CustomUser."""
    class Meta:
        model = CustomUser
        fields = (
            "username",
            "email",
        )  # listez ici les champs que vous utilisez


class UserFollowsForm(forms.Form):
    """Form for following another user."""
    username = forms.CharField(
        label="Nom d'utilisateur à suivre", max_length=150
    )
