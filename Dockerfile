FROM ghcr.io/hassio-addons/base-python:3.10

# Installation des dépendances
RUN pip install flask requests

# Copie des fichiers de l’add-on
COPY app /app
COPY www /www
COPY run.sh /run.sh

# Exécution du script
CMD [ "/run.sh" ]
