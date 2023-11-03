# Dockerfile pour Application Node.js

## Introduction

Ce Dockerfile est conçu pour construire une image Docker optimisée pour une application Node.js. Il détaille chaque étape de la construction de l'image pour fournir un environnement Node.js prêt à l'emploi.

## Construction de l'Image

### Image de Base

- **Image de Base**: `node:14`
  - Image Docker officielle avec Node.js version 14.
  - Fournit l'environnement Node.js nécessaire.

### Configuration du Répertoire de Travail

- **Répertoire de Travail**: `/usr/src/app`
  - Répertoire où les commandes seront exécutées et où les fichiers de l'application résideront.

### Gestion des Dépendances

- Copie des fichiers `package.json` et `package-lock.json` dans le répertoire de travail.
  - Définit les dépendances du projet Node.js.
  - Assure la cohérence des versions des dépendances avec `package-lock.json`.
- Exécution de `RUN npm install` pour installer les dépendances.

### Copie des Fichiers de l'Application

- Copie de tous les fichiers de l'application dans le répertoire de travail du conteneur.
  - Inclut les scripts, ressources et fichiers de code source.

### Exposition du Port

- Exposition du port `3000`.
  - Port standard pour les applications web Node.js.
  - Permet le mappage du port à l'hôte lors de l'exécution du conteneur.

## Démarrage de l'Application

- **Commande de Démarrage**: `CMD ["node", "app.js"]`
  - Lance l'application Node.js en exécutant le fichier `app.js` avec Node.js.

---

L'image Docker résultante est prête à exécuter l'application Node.js dans un environnement conteneurisé, assurant une mise en production rapide et efficace.
