# 测试data01.npy
# mlx90641
import matplotlib.pyplot as plt
import numpy as np
import paho.mqtt.subscribe as subscribe

np.random.seed(19971111)
data = np.random.random((100000, 64))
data01 = np.load("../Dataset/data03.npy")

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


fig, ax = plt.subplots()

for i in range(100000):
    ax.cla()
    piexls = data01[i]
    # piexls = receiveMqtt()
    # piexls.resize(12, 16)
    # print(piexls.max()," ",piexls.min()," ","温差：",piexls.max() - piexls.min(),"平均：",np.mean(piexls))
    ax.imshow(piexls, vmin=20, vmax=30)
    # ax.imshow(piexls, cmap="gray", vmin=20, vmax=35)
    # ax.imshow(data[i])
    ax.set_title("frame {}".format(i))
    # Note that using time.sleep does *not* work here!
    plt.pause(0.01)
#
# np.save("data01.npy",data)
