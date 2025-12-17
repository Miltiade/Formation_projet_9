from django.urls import path
from . import views

app_name = 'billets'

urlpatterns = [
    path('', views.flux_view, name='flux'),
    path('ajouter/', views.BilletCreateView.as_view(), name='ajouter'),
    path('modifier/<int:pk>/', views.BilletUpdateView.as_view(), name='modifier'),
    path('supprimer/<int:pk>/', views.BilletDeleteView.as_view(), name='supprimer'),
    path('<int:billet_pk>/commentaire/ajouter/', views.CommentaireCreateView.as_view(), name='commentaire_ajouter'),
    path('commentaire/<int:pk>/modifier/', views.CommentaireUpdateView.as_view(), name='commentaire_modifier'),
    path('commentaire/<int:pk>/supprimer/', views.CommentaireDeleteView.as_view(), name='commentaire_supprimer'),
]