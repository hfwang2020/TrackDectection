import paho.mqtt.client as mqtt
import time


# 连接成功回调
def on_connect(client, userdata, flags, rc):
    print('Connected with result code ' + str(rc))
    client.subscribe('sum')


# 消息接收回调
def on_message(client, userdata, msg):
    print(msg.topic + " " + str(msg.payload))


client = mqtt.Client(client_id="6b4deb575dc7e791470fb2c72a5432c0")

# 指定回调函数
client.on_connect = on_connect
client.on_message = on_message

# 建立连接
client.connect('42.192.171.165', 1883, 60)
# 发布消息
num = 1
while (1):
    client.loop()
    num += 1
    str1 = str(num) + "#"
    print(str1)
    client.publish('count', payload=str1, qos=0)
    time.sleep(0.5)
