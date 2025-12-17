from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic
from .forms import CustomUserCreationForm
from .forms import UserFollowsForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView
from .models import UserFollows
from django.contrib.auth import get_user_model
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views.generic import DeleteView


class SignUpView(generic.CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy("users:login")
    template_name = "users/signup.html"


def home(request):
    return render(request, "users/home.html")


class UserFollowsListView(LoginRequiredMixin, ListView):
    model = UserFollows
    template_name = "users/userfollows_list.html"
    context_object_name = "follows"

    def get_queryset(self):
        return UserFollows.objects.filter(user=self.request.user)


User = get_user_model()


@login_required
def userfollows_ajouter(request):
    if request.method == "POST":
        form = UserFollowsForm(request.POST)
        if form.is_valid():
            username_to_follow = form.cleaned_data["username"]
            try:
                user_to_follow = User.objects.get(username=username_to_follow)
                if user_to_follow == request.user:
                    messages.error(
                        request, "Vous ne pouvez pas vous suivre vous-même."
                    )
                else:
                    # Vérifier que le suivi n’existe pas déjà
                    existence = UserFollows.objects.filter(
                        user=request.user, followed_user=user_to_follow
                    ).exists()
                    if existence:
                        messages.error(
                            request, f"Vous suivez déjà {username_to_follow}."
                        )
                    else:
                        UserFollows.objects.create(
                            user=request.user, followed_user=user_to_follow
                        )
                        messages.success(
                            request,
                            f"Vous suivez maintenant {username_to_follow}.",
                        )
                        return redirect("users:userfollows_liste")
            except User.DoesNotExist:
                messages.error(
                    request,
                    f"L'utilisateur {username_to_follow} n'existe pas.",
                )
    else:
        form = UserFollowsForm()
    return render(request, "users/userfollows_form.html", {"form": form})


class UserFollowsDeleteView(LoginRequiredMixin, DeleteView):
    model = UserFollows
    template_name = "users/userfollows_confirm_delete.html"
    success_url = reverse_lazy("users:userfollows_liste")

    def get_queryset(self):
        # L’utilisateur connecté ne peut supprimer que ses propres suivis
        return UserFollows.objects.filter(user=self.request.user)
