import paho.mqtt.client as mqtt

# 连接成功回调
def on_connect(client, userdata, flags, rc):
    print('Connected with result code '+str(rc))
    client.subscribe('data')

# 消息接收回调
def on_message(client, userdata, msg):
    print(msg.topic+" "+str(msg.payload))

client = mqtt.Client(client_id="6b4deb575dc7e791470fb2c72a5432c0")

# 指定回调函数
client.on_connect = on_connect
client.on_message = on_message

# 建立连接
client.connect('bemfa.com', 9501, 60)
# 发布消息
client.publish('data01',payload='111',qos=0)

client.loop_forever()