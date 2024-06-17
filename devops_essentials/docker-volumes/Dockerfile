# Utiliser une image de base
FROM ubuntu:latest

# Installer des paquets nécessaires (optionnel)
RUN apt-get update && apt-get install -y \
    nano \
    && rm -rf /var/lib/apt/lists/*

# Créer un volume à /data
VOLUME /data

# Définir le répertoire de travail
WORKDIR /data

# Copier un script pour écrire/lire des données (optionnel)
COPY demo.sh /usr/local/bin/demo.sh
RUN chmod +x /usr/local/bin/demo.sh

# Commande pour garder le conteneur en cours d'exécution
CMD ["tail", "-f", "/dev/null"]
