from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser
from django import forms

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'email')  # listez ici les champs que vous utilisez

class UserFollowsForm(forms.Form):
    username = forms.CharField(label="Nom d'utilisateur à suivre", max_length=150)