from django import forms
from .models import Billet, Commentaire


class BilletForm(forms.ModelForm):
    class Meta:
        model = Billet
        fields = ["title", "description", "image"]


class CommentaireForm(forms.ModelForm):
    class Meta:
        model = Commentaire
        fields = ["headline", "body", "rating"]
