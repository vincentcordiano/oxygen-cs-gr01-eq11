# Étape 1 : Utilisez une image Alpine Linux légère
FROM python:3.9-alpine as builder

# Étape 2 : Copiez le code source et installez les dépendances
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Étape 3 : Supprimez les fichiers temporaires
RUN rm -rf /root/.cache

# Étape 4 : Image finale légère
FROM python:3.9-alpine
WORKDIR /app
COPY --from=builder /app /app

# Exécutez votre application
CMD ["python", "app.py"]
