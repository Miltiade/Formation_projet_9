from django.urls import path
from .views import BilletCreateView, HomeView
from django.views.generic import TemplateView

app_name = 'litrevu_app'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),  # la vue d’accueil
    path('billets/ajouter/', BilletCreateView.as_view(), name='billet_ajouter'),
    path('flux/', TemplateView.as_view(template_name='litrevu_app/flux.html'), name='flux'),
]