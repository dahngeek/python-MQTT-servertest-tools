# python-MQTT-servertest-tools

The toolset includes:
* A simple MQTT client with no authentication and a list of servers so you can add more than one for fallback.
* A simple MQTT data Generator with or without authentication.

### How to run:
```
pip install paho-mqtt
```
or
```
pip3 install paho-mqtt
```
depends on your python version.


Remember to **Modify** the client server in `mqtt-client.py` by changing `test.mosquitto.org` for your mqtt server.

**Modify** the generator server by modifying `config.json` also to your server settings.

then just run
```
python mqtt-client.py
```

or 
```
python mqttgen.py config.json
```



Thanks to mariano and eclipse paho docs for the initial code:

https://gist.github.com/marianoguerra/be216a581ef7bc23673f501fdea0e15a
https://www.eclipse.org/paho/index.php?page=clients/python/docs/index.php