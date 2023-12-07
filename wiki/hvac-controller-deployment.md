
# Configuration de Déploiement de Contrôleur HVAC

## Vue d'ensemble
Ce document explique la configuration de déploiement Kubernetes pour le déploiement d'un contrôleur HVAC.

## Détails de la Configuration

### apiVersion et kind
- `apiVersion: apps/v1` : Spécifie la version de l'API utilisée pour ce déploiement.
- `kind: Deployment` : Indique que ce fichier est pour une configuration de déploiement.

### Métadonnées
- `name`: Le nom du déploiement.
- `namespace`: L'espace de noms dans lequel ce déploiement sera créé.

### Spécification (spec)
- `replicas`: Le nombre de répliques de pod.
- `selector` : Utilise `matchLabels` pour sélectionner les bons pods.
- `template` : Décrit le modèle de pod à utiliser.

### Conteneurs
- Utilise l'image `log680gr11/oxygen:latest`.
- Expose le port 80.
- Définit des limites de ressources (CPU, mémoire).

## Choix d'Implémentation
Les choix spécifiques pour les images de conteneur, les ports, les variables d'environnement et les limites de ressources sont basés sur les exigences de l'application et les considérations de performance.

## Considérations pour le Déploiement
- **Environnement Kubernetes** : Assurez-vous que Kubernetes est configuré et que l'espace de noms spécifié existe.
- **Disponibilité des Ressources** : Vérifiez la disponibilité suffisante des ressources (CPU, mémoire) dans le cluster Kubernetes.
