import paho.mqtt.subscribe as subscribe
import numpy as np
import cv2
import time
import matplotlib.pyplot as plt
from PIL import Image
import matplotlib

# 把接收到的mqtt字符串转为numpy数组
def messageToArray(msg):
    msg_list = msg.split(sep=",")
    msg_list = msg_list[1:65]
    piexls = []
    for i in msg_list:
        piexls.append(float(i))
    newpiexls = np.array(piexls)
    newpiexls = np.resize(newpiexls, (8, 8))
    return newpiexls

while(1):
    #mqtt数据接收
    msg = subscribe.simple("test", hostname="192.168.1.115")
    a = messageToArray(str(msg.payload))
    #放大图片
    a = cv2.resize(a, None, None, fx=50, fy=50, interpolation=cv2.INTER_NEAREST)
    #显示图片
    plt.imshow(a, interpolation='None', cmap=plt.cm.gray, origin='upper')
    plt.colorbar()
    plt.xticks(())
    plt.yticks(())
    plt.show()



