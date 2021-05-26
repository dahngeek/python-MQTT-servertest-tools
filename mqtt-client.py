import paho.mqtt.client as mqtt



# The callback for when the client receives a CONNACK response from the server.

def on_connect(client, userdata, flags, rc):

        print("Connected with result code "+str(rc))

        # Subscribing in on_connect() means that if we lose the connection and

        # reconnect then subscriptions will be renewed.

        client.subscribe("hola", 0)



    # The callback for when a PUBLISH message is received from the server.

def on_message(client, userdata, msg):
    print(msg.topic+" "+str(msg.payload))

def on_subscribed(mosq, obj, mid, granted_qos):
    print("Subscribed mid: " + str(mid) + ", qos: " + str(granted_qos))



client = mqtt.Client()

client.on_connect = on_connect

client.on_message = on_message

client.on_subscribed = on_subscribed

def conectar(id):
    servidores = ["test.mosquitto.org"]
    try:
        print("Probando conectar a "+servidores[id])
        client.connect(servidores[id], 1883)
    except KeyboardInterrupt:
        return
    except:
        print("Fallo.")
        if id < len(servidores):
            conectar(id+1)
        else:
            conectar(0)

def on_disconnect(client, userdata, rc):
    if rc != 0:
        print("Desconexion no esperada.")
        print("Tratando de reconectar.")
        conectar(0)

client.on_disconnect = on_disconnect

conectar(0)

# client.subscribe("hola", 0)

    # Blocking call that processes network traffic, dispatches callbacks and

    # handles reconnecting.

    # Other loop*() functions are available that give a threaded interface and a

    # manual interface.

client.loop_forever()