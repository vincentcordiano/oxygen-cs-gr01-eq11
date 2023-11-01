# Utilisez une image Python officielle
FROM python:3.8

# Définissez le répertoire de travail
WORKDIR /app

# Copiez les fichiers Python dans le conteneur
COPY . .

# Installez les dépendances Python (si nécessaire)
# RUN pip install -r requirements.txt

# Exécutez le script Python au démarrage
CMD ["python", "main.py"]
