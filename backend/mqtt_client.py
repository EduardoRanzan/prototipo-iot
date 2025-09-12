import paho.mqtt.client as mqtt

# Callback quando uma mensagem chega
def on_message(client, userdata, msg):
    print(f"[MQTT] Tópico: {msg.topic} | Mensagem: {msg.payload.decode()}")

def main():
    client = mqtt.Client()
    client.on_message = on_message
    client.connect("localhost", 1883)  # Mosquitto no Docker
    client.subscribe("iot/sensors")   # Tópico para ouvir

    print("[MQTT] Aguardando mensagens...")
    client.loop_forever()

if __name__ == "__main__":
    main()
