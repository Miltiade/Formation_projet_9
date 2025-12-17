from django.urls import path
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView, LogoutView
from .views import SignUpView
from . import views

app_name = "users"

urlpatterns = [
    path(
        "login/",
        LoginView.as_view(template_name="users/login.html"),
        name="login",
    ),
    path(
        "logout/",
        LogoutView.as_view(next_page=reverse_lazy("users:login")),
        name="logout",
    ),
    path("signup/", SignUpView.as_view(), name="signup"),
    path(
        "suivis/",
        views.UserFollowsListView.as_view(),
        name="userfollows_liste",
    ),
    path(
        "suivis/ajouter/",
        views.userfollows_ajouter,
        name="userfollows_ajouter",
    ),
    path(
        "suivis/<int:pk>/supprimer/",
        views.UserFollowsDeleteView.as_view(),
        name="userfollows_supprimer",
    ),
]
