# Pipeline Metrics

Ce fichier .md explique deux workflows distincts gérés par GitHub Actions : `ci.yml` et `docker.yml`, qui automatisent les étapes de construction, de test, et de déploiement d'une application. Le pipeline est déclenché automatiquement sur la branche principale (main) du référentiel à chaque push.

## Workflow CI (`ci.yml`)

Le workflow CI est responsable de la construction, des tests, et de la vérification de la qualité du code. Voici les étapes de ce workflow :

### Étape 1 : Checkout du code
- Utilisation de l'action [`actions/checkout@v2`](https://github.com/actions/checkout) pour récupérer le code source depuis le référentiel.

### Étape 2 : Configuration de Python
- Utilisation de l'action [`actions/setup-python@v2`](https://github.com/actions/setup-python) pour configurer Python. La version Python 3.8 est utilisée ici, mais vous pouvez la remplacer par la version Python que vous utilisez.

### Étape 3 : Installation des dépendances
- Installation des dépendances Python à partir du fichier `requirements.txt`.
- Installation de la bibliothèque `psycopg2`.

### Étape 4 : Exécution des tests
- Exécution des tests en utilisant la commande `python test/test.py`. La valeur `exit 0` indique que le workflow se terminera avec succès même si les tests échouent.

### Étape 5 : Lint et formatage du code
- Installation des outils `pylint` et `black`.
- Vérification de la qualité du code en exécutant `pylint` sur le fichier `src/main.py`.
- Vérification du format du code en exécutant `black --check` sur le fichier `src/main.py`.

## Workflow Docker Build and Push (`docker.yml`)

Le workflow Docker Build and Push est responsable de la construction d'une image Docker et de sa publication sur DockerHub. Voici les étapes de ce workflow :

### Étape 1 : Checkout du code
- Tout comme dans le workflow CI, le code source est récupéré depuis le référentiel.

### Étape 2 : Configuration de Docker Buildx
- Utilisation de l'action [`docker/setup-buildx-action@v1`](https://github.com/docker/setup-buildx-action) pour configurer Docker Buildx.

### Étape 3 : Connexion à DockerHub
- Utilisation des secrets GitHub (`secrets.DOCKERHUB_USERNAME` et `secrets.DOCKERHUB_PASSWORD`) pour se connecter à DockerHub.

### Étape 4 : Construction et publication de l'image Docker
- Construction de deux images Docker avec les étiquettes `log680gr11/oxygen:latest` et `log680gr11/oxygen:1.0`.
- Les images sont ensuite poussées vers DockerHub pour être accessibles.

Ces deux workflows assurent la construction, les tests et le déploiement de votre application de manière automatisée. Ils garantissent que le code est testé, formaté correctement, et que les images Docker sont construites et disponibles pour le déploiement.
