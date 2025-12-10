from django.db import models
from django.conf import settings
from django.core.validators import MinValueValidator, MaxValueValidator

class Billet(models.Model):
    # Titre du billet, champ texte limité à 128 caractères
    title = models.CharField(max_length=128)

    # Description complète du billet, champ texte limité à 2048 caractères
    description = models.TextField(max_length=2048, blank=True)

    # Auteur du billet, liaison vers le modèle utilisateur Django
    # on_delete=models.CASCADE signifie que si l'utilisateur est supprimé, ses billets le sont aussi
    user = models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    # Image associée au billet, optionnelle (blank=True, null=True)
    # upload_to définit le dossier où l’image sera stockée
    image = models.ImageField(upload_to='images/', blank=True, null=True)

    # Date et heure de création automatique du billet
    time_created = models.DateTimeField(auto_now_add=True)

    # Méthode pour afficher le titre dans l’administration ou les listes
    def __str__(self):
        return self.title


class Commentaire(models.Model):
    # Billet auquel ce commentaire est associé
    billet = models.ForeignKey(to='Billet', on_delete=models.CASCADE, related_name='commentaires')

    # Note attribuée au billet (par exemple, un entier)
    rating = models.PositiveSmallIntegerField(validators=[MinValueValidator(0), MaxValueValidator(5)])

    # Utilisateur auteur du commentaire
    user = models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    # Titre du commentaire
    headline = models.CharField(max_length=128)

    # Texte du commentaire
    body = models.TextField(max_length=8192, blank=True)

    # Date et heure de création automatique
    time_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.headline} ({self.rating}/5)'