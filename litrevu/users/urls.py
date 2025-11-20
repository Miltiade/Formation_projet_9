# définir les URL pour la connexion et la déconnexion en utilisant les vues intégrées de Django

from django.urls import path
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView, LogoutView

app_name = 'users'

urlpatterns = [
    path('login/', LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', LogoutView.as_view(next_page=reverse_lazy('users:login')), name='logout'),
]