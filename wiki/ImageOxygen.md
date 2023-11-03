# Dockerfile pour Application Python

## Introduction

Ce Dockerfile est conçu pour créer une image Docker légère et sécurisée pour une application Python, en utilisant plusieurs étapes pour optimiser la taille et l'efficacité de l'image finale.

## Construction de l'Image

### Étape 1: Image de Base

- **Image de Base**: `python:3.9-alpine`
  - Utilisation d'Alpine Linux pour sa petite taille et sa sécurité.
  - Python 3.9 est préinstallé.

### Étape 2: Installation des Dépendances

- Création d'un répertoire de travail (`/app`).
- Copie du fichier `requirements.txt` dans le conteneur.
- Utilisation de `pip` pour installer les dépendances listées dans `requirements.txt`.
  - Installation sans conserver de cache pour minimiser la taille de l'image.

### Étape 3: Nettoyage

- Suppression des fichiers temporaires et des caches créés pendant l'installation.
  - Assure que l'image ne contient aucun fichier inutile.

### Étape 4: Image Finale

- Création de l'image finale à partir de l'image de base Alpine Python.
- Copie du répertoire de travail depuis l'étape de construction vers le nouveau conteneur.
  - L'image finale contient uniquement le code de l'application et ses dépendances.

## Exécution du Conteneur

- **Commande de Démarrage**: Exécution de l'application Python (`app.py`).

---

Le Dockerfile décrit ici permet de déployer une application Python dans un environnement Docker optimisé pour la sécurité et la légèreté.
