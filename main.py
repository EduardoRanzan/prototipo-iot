import paho.mqtt.client as mqtt
from influxdb import InfluxDBClient
import json

# Configuração do InfluxDB
client = InfluxDBClient(host='localhost', port=8086, database='iot_db')

# Função chamada quando chega uma mensagem MQTT
def on_message(client_mqtt, userdata, msg):
    data = json.loads(msg.payload.decode())
    json_body = [
        {
            "measurement": "sensor_data",
            "tags": {
                "device_id": data["device_id"],
                "location": data["location"]
            },
            "fields": {
                "temperature": float(data["temperature"]),
                "humidity": float(data["humidity"]),
                "luminosity": int(data["luminosity"])
            }
        }
    ]
    client.write_points(json_body)

# Configuração do MQTT
mqtt_client = mqtt.Client()
mqtt_client.on_message = on_message
mqtt_client.connect("localhost", 1883, 60)
mqtt_client.subscribe("iot/sensors")
mqtt_client.loop_forever()
