FROM python:3.9-alpine as builder

# Copiez le code source et installez les dépendances
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Supprimez les fichiers temporaires
RUN rm -rf /root/.cache

# Image finale légère
FROM python:3.9-alpine
WORKDIR /app
COPY --from=builder /app .

CMD ["echo", "Container created"]
