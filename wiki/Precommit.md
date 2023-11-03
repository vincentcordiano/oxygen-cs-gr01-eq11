# Script de Pré-Commit pour Git

## Objectif

Le script de pré-commit est un outil automatisé qui s'exécute avant chaque `commit` dans Git. Son but est de s'assurer que le code soumis respecte les normes de qualité établies et est exempt d'erreurs et d'incohérences.

## Fonctionnalités du Script

### Vérification du Code avec Pylint

- **Pylint**: Analyse le code pour identifier les erreurs, les codes qui ne sont pas idiomatiques et les problèmes de style.
  - Bloque le commit si des problèmes sont détectés.

### Formatage du Code avec Black

- **Black**: Formate le code pour qu'il suive un standard uniforme.
  - Assure la cohérence du style de codage à travers le projet.

### Exécution des Tests Unitaires

- **Tests Unitaires**: Exécute la suite de tests pour détecter les régressions.
  - Prévient l'introduction de bugs dans le dépôt.

## Processus de Vérification

1. **Pylint** est exécuté pour analyser le code.
2. **Black** est utilisé pour formater le code automatiquement.
3. Les **tests unitaires** sont lancés pour confirmer la stabilité fonctionnelle.

## Gestion des Erreurs

- En cas d'erreur détectée par l'une des étapes, le script bloque le commit.
- Un message est affiché pour demander des corrections.
- Le développeur doit résoudre les problèmes avant de pouvoir commit.

## Avantages

- Garantit l'intégrité et la propreté du code dans le dépôt.
- Encourage les bonnes pratiques de développement.
- Réduit le risque d'introduire des erreurs dans la base de code principale.

---

Ce script de pré-commit est un élément essentiel pour maintenir la qualité et la fiabilité du code dans les projets utilisant Git.
