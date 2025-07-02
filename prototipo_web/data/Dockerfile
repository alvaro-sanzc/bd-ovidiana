FROM tenforce/virtuoso

USER root

# Instala netcat y bash
RUN apt-get update && \
    apt-get install -y netcat bash && \
    rm -rf /var/lib/apt/lists/*

# Asegura los permisos y crea directorios necesarios
RUN mkdir -p /data /rdf /scripts && chmod -R 777 /data /rdf /scripts

WORKDIR /data
