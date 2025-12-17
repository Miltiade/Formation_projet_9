"""
Views for Billet and Commentaire models.
"""

from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView
from .models import Billet, Commentaire
from users.models import UserFollows
from django.shortcuts import get_object_or_404
from .forms import BilletForm, CommentaireForm
from django.contrib.auth.decorators import login_required


class BilletCreateView(LoginRequiredMixin, CreateView):
    """View for creating a new Billet."""
    model = Billet
    form_class = BilletForm
    template_name = "billets/billet_form.html"  # créez ce template
    success_url = reverse_lazy(
        "billets:flux"
    )  # ajustez la redirection après ajout

    def form_valid(self, form):
        form.instance.user = (
            self.request.user
        )  # associe le billet à l’utilisateur connecté
        return super().form_valid(form)


class BilletUpdateView(LoginRequiredMixin, UpdateView):
    """View for updating an existing Billet."""
    model = Billet
    form_class = BilletForm
    template_name = "billets/billet_form.html"
    success_url = reverse_lazy("billets:flux")

    def get_queryset(self):
        return Billet.objects.filter(
            user=self.request.user
        )  # permet uniquement à l’auteur de modifier


class BilletDeleteView(LoginRequiredMixin, DeleteView):
    """View for deleting a Billet."""
    model = Billet
    template_name = "billets/billet_confirm_delete.html"  # créez ce template
    success_url = reverse_lazy("billets:flux")

    def get_queryset(self):
        return Billet.objects.filter(
            user=self.request.user
        )  # permet uniquement à l’auteur de supprimer


@login_required
def flux(request):
    billets = Billet.objects.all().order_by(
        "-time_created"
    )  # trie les billets par date de création décroissante
    return render(request, "billets/flux.html", {"billets": billets})


class CommentaireCreateView(LoginRequiredMixin, CreateView):
    """View for creating a new Commentaire associated with a Billet."""
    model = Commentaire
    form_class = CommentaireForm
    template_name = "billets/commentaire_form.html"

    def dispatch(self, request, *args, **kwargs):
        # Récupère le billet associé ou retourne 404 si inexistant
        self.billet = get_object_or_404(Billet, pk=kwargs["billet_pk"])
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        form.instance.user = (
            self.request.user
        )  # associe l’utilisateur connecté
        form.instance.billet = self.billet  # associe le billet
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy(
            "billets:flux"
        )  # ou vers une page billet précise si vous préférez


class CommentaireUpdateView(LoginRequiredMixin, UpdateView):
    """View for updating an existing Commentaire."""
    model = Commentaire
    form_class = CommentaireForm
    template_name = "billets/commentaire_form.html"

    def get_queryset(self):
        # Seuls les auteurs peuvent modifier leurs commentaires
        return Commentaire.objects.filter(user=self.request.user)

    def get_success_url(self):
        return reverse_lazy("billets:flux")


class CommentaireDeleteView(LoginRequiredMixin, DeleteView):
    """View for deleting a Commentaire."""
    model = Commentaire
    template_name = "billets/commentaire_confirm_delete.html"  # à créer
    success_url = reverse_lazy("billets:flux")

    def get_queryset(self):
        # Autoriser uniquement l’auteur du commentaire à le supprimer
        return Commentaire.objects.filter(user=self.request.user)


@login_required
def flux_view(request):
    """Function-based view to display a combined feed of Billets and Commentaires"""
    # Étape 1 : récupérer les IDs des utilisateurs suivis
    suivis = UserFollows.objects.filter(user=request.user).values_list(
        "followed_user", flat=True
    )

    # Étape 2 : récupérer billets de l'utilisateur courant + users suivis
    billets = Billet.objects.filter(user__in=list(suivis) + [request.user.id])

    # Étape 3 : récupérer commentaires (utilisateur+suivis) desdits billets
    commentaires = Commentaire.objects.filter(
        user__in=list(suivis) + [request.user.id], billet__in=billets
    )

    # Étape 4 : fusionner et trier par date de création descendante
    flux = list(billets) + list(commentaires)
    flux_tries = sorted(flux, key=lambda x: x.time_created, reverse=True)

    # Étape 5 : passer la liste au template pour affichage
    return render(request, "billets/flux.html", {"flux": flux_tries})
