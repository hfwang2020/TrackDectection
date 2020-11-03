# 采集数据

import numpy as np
import paho.mqtt.subscribe as subscribe
import time


def receiveMqtt():
    msg = subscribe.simple("test", hostname="192.168.1.120")
    msg = str(msg.payload)
    msg_list = msg.split(sep=",")
    msg_list = msg_list[1:193]
    piexls = []
    for i in msg_list:
        piexls.append(float(i))
    piexls1 = np.array(piexls)
    return piexls1


data = np.random.random((1000, 12, 16))

for i in range(1000):
    piexls = receiveMqtt()
    piexls.resize(12, 16)
    data[i] = piexls
    time.sleep(0.05)


# 单人通过数据
np.save('../Dataset/data04.npy', data)

# 双人通过数据
# np.save("../Dataset/data02.npy",data)
