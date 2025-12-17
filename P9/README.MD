# LITRevu - Application de critiques de livres

LITRevu est une application web développée avec Django permettant aux utilisateurs de publier, consulter et commenter des critiques de livres et d’articles.

## Pré-requis

- Python 3.8 ou supérieur  
- pip (gestionnaire de paquets Python)  
- Un environnement virtuel (par exemple : venv)  

## Installation

1. Clonez ce repository :  
   ```bash
   git clone https://github.com/votre-utilisateur/votre-repo.git
   cd votre-repo
   ```

2. Créez un environnement virtuel et activez-le :

   ```bash
   python -m venv env
   source env/bin/activate  # sur macOS/Linux
   env\Scripts\activate     # sur Windows
   ```

3. Installez les dépendances :

   ```bash
   pip install -r requirements.txt
   ```

## Initialisation de la base de données

1. Appliquez les migrations Django :

   ```bash
   python manage.py migrate
   ```

2. (Optionnel) Créez un super utilisateur :

   ```bash
   python manage.py createsuperuser
   ```

## Lancement du serveur

1. Démarrez le serveur de développement :

   ```bash
   python manage.py runserver
   ```

2. Ouvrez ensuite votre navigateur à l’adresse [http://127.0.0.1:8000/](http://127.0.0.1:8000/) pour accéder à l’application.

## Fonctionnalités principales

- Inscription et connexion des utilisateurs
- Création, modification et suppression de billets (critiques)
- Ajout et gestion des commentaires sur les billets
- Suivi d’autres utilisateurs et affichage d’un flux personnalisé
- Gestion des droits d’accès pour assurer la sécurité des données

## Conseils d’utilisation

- Seuls les utilisateurs inscrits peuvent écrire, modifier ou supprimer leurs billets et commentaires.
- Dans l’interface d’administration Django (`/admin`), vous pouvez gérer les utilisateurs et contenus si vous avez les droits.

## Accessibilité

L’application suit les recommandations d’accessibilité WCAG.

## Ressources

- Documentation Django : https://docs.djangoproject.com/
