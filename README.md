# README | HAIROLOGY


## Auteurs : 
Lea Chaoui (programmation)
Mathis Chappell (implementation du scan)
Morjana Benyahia (maquette (choix de mise en page et palette) 
Laetitia Abotsi (expertise en capillaire et preparation de produits et ingredients)


## Description du projet:
HAIROLOGY, l’assistant capillaire intelligent qui sécurise ta routine
« Simple, smart, et pensé pour une beauty routine sans risques »
Une application web et mobile permettant de :
- Scanner (ou d’entrer manuellement) des produits capillaires à l’aide d’un code-barres
- Entrer manuellement leur code EAN 
- Analyser leur compatibilité avec nos précieux cheveux
- Enregistrer au fur et à mesure les produits qu’il utilise. Les produits sont sauvegardés sur son compte, ce qui lui permet de vérifier dans le temps s’ils sont compatibles entre eux.


## Structure du projet :
- Dossier Hairology :
        - README.md
        - app.py
        - seed.py
        - database.db
        - Dossier templates :
                - index.html
                - signup.html
                - login.html
                - profil.html 
                - scan.html
        - Dossier static :
                - scan.js 
                - Dossier images :
                        - images de type cheveux : 1a.png , 1b.png , 1c.png , 2a.png , 2b.png , 2c.png , 3a.png , 3b.png , 3c.png , 4a.png , 4b.png , 4c.png
                        - images de profil par défaut : default_femme.png , default_homme.png , default_autre.png
        - Dossier __pycache__ :
                - app.cpython-314


## Fonctionnalités 
- Interface simple et esthétique
- Page d’accueil avec accès au scan (après authentification)
- Pages d’inscription et de connexion
- Possibilité d’ajout des nouveaux produits non reconnus (qui s’ajoutent à la base de données globale, donc qui s’actualise pour tous les utilisateurs)
- Profil utilisateur avec collection des produits ajoutés avec date d’ajout et d’utilisation
- Saisie manuelle du code EAN (la méthode utilisée sur PC lors de la démonstration vidéo Hairology_video.mp4.)
- Scan de code-barres via la caméra (mobile et ordinateur) avec Design et fonctionnement inspirés d’Inci Beauty 
- Détection d’incompatibilités des produits selon la base d’ingrédients incompatibles


## Technologies utilisées 
- Prérequis : Python, Modules python (Flask, Sqlite3), Un navigateur (Chrome, Firefox…)
- HTML : 5 fichiers (index.html, signup.html, login.html, profil.html et scan.html)
- CSS intégré dans les pages html
- JavaScript (et QuaggaJS) : 1 fichier scan.js
- Base de données : 1 fichier SQLite database.db (actualisable et modifiable, à partir de seed.py et de la session utilisateur)
- Python : 2 fichiers (app.py et seed.py)


## Installation
1. Télécharger le fichier ZIP du projet et l’extraire 
2. Si nécessaire, réinitialiser la base de données database.db :
    - Supprimer database.db 
    - Lancer seed.py pour créer la base (sur le terminal : python seed.py)
3. Lancer également l’application Flask (via le terminal : python app.py)
4. Le terminal affichee un lien : (ex Running on http://127.0.0.1:5000/)
5. Ouvrir ce lien dans un navigateur, directement sur la page d’accueil, prêt à être utilisé
### Remarque :  
Les étapes 2, 3, 4 et 5 sont démontrées dans la vidéo Hairology_video.mp4  


## Utilisation
1. Accéder à l’application via le lien renvoyé par Flask (regarder étape 4 d’installation) 
2. Créer un compte ou alors se connecter  
3. Cliquer sur le bouton « scanner un produit » 
4. Autoriser l’accès à la caméra
5. Scanner le code-barres du produit ou saisir le code EAN manuellement et appuyez sur « analyser »
6. Vérifier les informations du produit (Le nom du produit, la marque, les ingrédients, et s’il est compatible ou pas avec le reste des produits dans votre collection)
7. Enregistrer les informations sur le profil en appuyant sur « ajouter à ma collection » 
7. Retrouver les informations sur le profil utilisateur dans l’onglet « Mes produits enregistrés »
8. Répéter le processus pour scanner et analyser d’autres produits
### Astuce :
Le scan fonctionne mieux sur mobile ou avec une bonne luminosité.


## Vidéo de démonstration
Pour plus de compréhension, veuillez regarder la vidéo sur l’utilisation de l’application HAIROLOGY 
[Hairology_video.mp4] (https://www.swisstransfer.com/d/cb8ec77b-2288-4d57-bef0-730869d622fb)
-> à télécharger sur SwissTransfert « attention ! le lien s’expire le 17/02/2026 à 19:23 »


## Auteurs : 
Etudiants du bachelor technologie et management , 3ème année 
Lea Chaoui, Mathis Chappell, Morjana Benyahia, Laetitia Abotsi
le 18/01/2026
