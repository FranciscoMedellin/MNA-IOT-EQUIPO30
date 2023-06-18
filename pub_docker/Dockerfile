# Imagen base
FROM python:3.9

# Directorio de trabajo
WORKDIR /app

# Copiar archivos al contenedor
COPY pub_docker.py requirements.txt /app/

# Instalar dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Exponer el puerto de comunicacion
EXPOSE 1883

# Comando por defecto para ejecutar el cliente MQTT
CMD ["python", "pub_docker.py"]
