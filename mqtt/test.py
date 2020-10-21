import paho.mqtt.client as mqtt
import _thread
import numpy as np
import os

sub_Message = ""
# 连接成功回调
def on_connect(client, userdata, flags, rc):
    print('Connected with result code ' + str(rc))
    client.subscribe('test')

# 消息接收回调
def on_message(client, userdata, msg):
    # print(msg.topic + " " + str(msg.payload))
    sub_Message = str(msg.payload)
    a = messageToArray(sub_Message)
    print(a)
    print(type(a))

    # f = open("db.txt",mode="a")
    # f.write(str(msg.payload))
    # f.write("\r\n")
    # f.close()

#str(msg.payload)转为numpy.array
def messageToArray(msg):
    msg_list = msg.split(sep=",")
    msg_list = msg_list[1:65]
    piexls = []
    for i in msg_list:
        piexls.append(float(i))

    return piexls

client = mqtt.Client()
# 指定回调函数
client.on_connect = on_connect
client.on_message = on_message
# 建立连接
client.connect('192.168.1.102', 1883, 60)
# 发布消息
client.loop_forever()

