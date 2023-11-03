# Tests Unitaires pour le Système de Gestion CVC/HVAC

## Introduction

Ce document décrit une suite de tests unitaires pour le système de gestion CVC/HVAC en utilisant le framework `unittest` de Python. Ces tests sont conçus pour valider le comportement de la classe `Main`.

## Configuration des Tests

### Méthode `setUp`

- Création d'une instance de la classe `Main`.
- Remplacement de la connexion au hub par un objet fictif (`MagicMock`) pour isoler les tests des dépendances externes.

## Méthodes de Test

### `test_take_action_turn_on_ac`

- Vérifie que la méthode `take_action` active la climatisation lorsque la température dépasse le seuil maximum.
- Confirmation par la vérification de l'appel à `send_action_to_hvac` avec les arguments corrects.

### `test_take_action_turn_on_heater`

- Vérifie que la méthode `take_action` active le chauffage lorsque la température est en dessous du seuil minimum.
- Confirmation par la vérification de l'appel à `send_action_to_hvac` avec les arguments corrects.

### `test_take_action_do_nothing`

- S'assure qu'aucune action n'est déclenchée si la température est dans la plage acceptable.
- Validation par la vérification que `send_action_to_hvac` n'est pas appelée.

## Interaction avec l'API HVAC et la Base de Données

### Utilisation de `patch`

- Remplacement des appels réseau et des connexions à la base de données par des objets fictifs pour les tests.

### `test_send_action_to_hvac`

- Simulation d'une réponse de l'API HVAC.
- Vérification que l'événement est correctement enregistré dans la base de données.

### `test_send_temperature_to_database`

- Assurance que les données de température sont correctement insérées dans la base de données.

### `test_send_event_to_database`

- Assurance que les événements sont correctement insérés dans la base de données avec les requêtes SQL appropriées.

---

Ces tests unitaires garantissent que la classe `Main` fonctionne comme prévu, indépendamment des services externes et des interactions réseau.
