# Système de Gestion HVAC

## Description

Le script Python décrit ci-dessous fait partie d'un système de gestion de chauffage, ventilation et climatisation (CVC/HVAC). Il est conçu pour automatiser le contrôle de la température à l'aide d'une classe principale nommée `Main`.

### Initialisation

Lors de la création d'une instance de la classe `Main`, plusieurs paramètres sont initialisés :

- `HOST`: L'adresse du serveur.
- `Token d'authentification`: Pour l'authentification sécurisée.
- `Seuils de température`: Valeurs maximales et minimales pour le contrôle de la température.
- `Détails de connexion à PostgreSQL`: Pour la connexion à la base de données.

Ces paramètres sont essentiels pour établir une connexion avec le hub de données de capteurs et pour déterminer les actions à prendre en fonction des lectures de température.

### Configuration

La méthode `setup` est utilisée pour configurer la connexion au hub de données de capteurs.

### Exécution

Après la configuration, la méthode `start` est appelée. Elle établit la connexion au hub et démarre une boucle infinie qui permet au script de fonctionner continuellement, recevant et traitant les données de température en temps réel.

### Gestion des Événements

La connexion au hub est conçue pour écouter les données des capteurs et gérer les événements tels que :

- Ouverture de la connexion.
- Fermeture de la connexion.
- Erreurs potentielles.

### Traitement des Données

Lors de la réception des données des capteurs, la méthode `on_sensor_data_received` est invoquée. Elle effectue les opérations suivantes :

- Affichage des données.
- Prise de décision basée sur la température actuelle.
- Envoi des informations à la base de données.

### Contrôle de Température

- **Activation de la climatisation** : Si la température dépasse le seuil maximum.
- **Activation du chauffage** : Si la température tombe en dessous du seuil minimum.

Toutes les actions et les lectures de température sont enregistrées dans la base de données.

---

Ce document décrit le fonctionnement d'un script Python pour la gestion d'un système HVAC.
