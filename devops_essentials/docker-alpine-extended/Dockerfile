# Utiliser l'image de base Alpine
FROM alpine:latest

# Installer le package curl
RUN apk add --no-cache curl

# Copier le fichier config.txt dans le conteneur
COPY config.txt /app/config.txt

# Définir le point d'entrée (facultatif)
CMD ["/bin/sh"]
