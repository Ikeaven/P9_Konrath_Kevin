# P9_Konrath_Kevin
Développez une application Web en utilisant Django :

L’application permet de :
demander des critiques de livres ou d’articles, en créant un ticket ;
publier des critiques de livres ou d’articles


## 1. Récupérer le projet :


    $ git clone https://github.com/Ikeaven/P9_Konrath_Kevin.git

Se déplacer dans le repertoire du projet :

    $ cd P9_Konrath_Kevin

## 2. Créer et activer un environnement virtuel :

    $ python3 -m venv env


Sous macOS ou Linux :

    $ . env/bin/activate

Sous Windows :

    $ env\Scripts\activate.bat
## 3. Installer les dépendances :

    $ pip install -r requirements.txt

## 4. Créer un super user :

    $ cd LITReview/
    $ ./manage.py createsuperuser

Suivre les indications de la console.
Une fois le super user créé, vous pouvez vous connecter à l'espace d'admin du site grâce à son identifiant et mot de passe. Mais avant il faut encore démarrer le serveur de developpement.

## 5. Démarrer le serveur de developpement :

On est toujours dans le dossier du projet LITReview.

    $  ./manage.py runserver

Le site sera accéssible à l'adresse local : 127.0.0.1:8000 sur le port 8000 par défaut.
Si le port n'est pas disponible :

    $ ./manage.py runserver <your_port>

## 6. Naviguer vers l'éspace d'administration

Ouvrir un navigateur, et aller à l'adresse du site en ajouter /admin.
ex : http://127.0.0.1:8000/admin/

Entrez l'identifiant et le mot de passe du super user créé à la partie 4.

## 7. Naviguer sur le site

Ouvrir un navigateur, et aller à l'adresse du site.
ex : http://127.0.0.1:8000/