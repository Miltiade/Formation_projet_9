"""
Forms for Billet and Commentaire models.
"""

from django import forms
from .models import Billet, Commentaire


class BilletForm(forms.ModelForm):
    """Form for creating or updating Billet instances."""
    class Meta:
        model = Billet
        fields = ["title", "description", "image"]


class CommentaireForm(forms.ModelForm):
    """Form for creating or updating Commentaire instances."""
    class Meta:
        model = Commentaire
        fields = ["headline", "body", "rating"]
