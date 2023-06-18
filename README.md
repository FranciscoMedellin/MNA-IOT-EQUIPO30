# MNA-IOT-EQUIPO30

En este repositorio se incluyen lo siguiente:
- Archivos para la creacion de una imagen de docker que simule dispositivos pub mqtt.
- Notebook en colab de un cliente sub mqtt para la lectura de la data publicada en el broker desde los dispositivos.

## Instrucciones de uso
- Abre una terminal en la ruta donde se encuentra el folder pub_docker.
- Ejecuta el siguiente comando:
```
docker build pub_docker
```
- Una vez terminada la ejecucion verifica el ID de tu imagen, ejecuta:
```
docker ps 
```
- En caso de que la imagen no tenga nombre se vera como: <none>
- Para colocar el nombre a la imagen ejecuta el siguiente comando:
```
docker tag <IMAGE_ID> <NOMBRE>:<ETIQUETA> 
```
```
docker tag <IMAGE_ID> pub-docker:latest
```
- Ejecutar un contenedor con la imagen de docker para simular un dispositivo:
```
docker run -p 1883:1883 -e DEVICE="device1"  pub_docker python pub_docker.py
```
- Obtener el ID del contenedor:
```
docker container ps
```
- Detener el contenedor:
```
docker container stop <CONTAINER_ID>
```
