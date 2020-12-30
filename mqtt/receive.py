import paho.mqtt.client as mqtt

def on_connect(client, userdata, flags, rc):
    print("Connected with result code: " + str(rc))

def on_message(client, userdata, msg):
    print(msg.topic + " " + str(msg.payload))

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.connect('42.192.171.165', 1883, 600) # 600为keepalive的时间间隔
client.subscribe('hz', qos=0)
# client.subscribe('')
client.subscribe('count')
client.loop_forever()
