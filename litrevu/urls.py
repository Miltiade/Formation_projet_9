from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include('users.urls', namespace='users')),  # app users
    path('', include('litrevu_app.urls', namespace='litrevu')),  # votre app principale
]

print("Chargement du fichier urls.py racine")
