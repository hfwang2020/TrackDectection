import paho.mqtt.subscribe as subscribe
import numpy as np


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
