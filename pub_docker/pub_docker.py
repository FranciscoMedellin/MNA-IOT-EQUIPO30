#importación de librerías
import time
import os
import logging as lg
import random
import paho.mqtt.client as mqttClient


Connected = False
broker_address= "broker.hivemq.com" #"8.tcp.ngrok.io" # "broker.hivemq.com"  #broker público
port= 1883 #12105 #1883  # puerto por defecto

tag_broker= "MNA/IoT/2023/MQTT/Equipo30/"
device = os.environ.get("DEVICE") #"device1"
tag1 = tag_broker + device + "/Temperatura" #"MNA/IoT/Equipo30/device1/Temperatura"
tag2 = tag_broker + device + "/Humedad" #"MNA/IoT/Equipo30/device1/Humedad"

def get_temp():
    return random.randint(0, 45)

def get_hum():
    return random.randint(8, 99)

def on_connect(client,userdata,flags,rc):
    """Función que establece la conexión
    """
    if rc==0:
        lg.info("Conectado al broker")
        global Connected
        Connected = True
    else:
        lg.info("Falla en la conexión al broker")
    return

client = mqttClient.Client("publicador")
client.on_connect = on_connect
client.connect(broker_address,port)
client.loop_start() #inicializar

while Connected != True:
    time.sleep(0.2)
    try:
        try:
            while  True:
                lg.info("DEVICE NAME: ",device)
                val1 = get_temp()
                val2 = get_hum() 
                lg.info(tag1,val1,"\n",tag2,val2,"\n")
                client.publish(tag1,val1, qos=0)
                client.publish(tag2,val2, qos=0)
                lg.info("data publicada")
                time.sleep(2)
        except:
            lg.info("Envio de datos suspendido")
            client.disconnect()
            client.loop_stop()
    except KeyboardInterrupt:
        lg.info("Envío de datos suspendido por el usuario")
        client.disconnect()
        client.loop_stop()