# 实时测试
import matplotlib.pyplot as plt
import numpy as np
import paho.mqtt.subscribe as subscribe

np.random.seed(19971111)
data = np.random.random((100000, 64))


def receiveMqtt():
    msg = subscribe.simple("test", hostname="192.168.1.120")
    msg = str(msg.payload)
    msg_list = msg.split(sep=",")
    msg_list = msg_list[1:65]
    piexls = []
    for i in msg_list:
        piexls.append(float(i))
    piexls1 = np.array(piexls)
    return piexls1


fig, ax = plt.subplots()

for i in range(100000):
    ax.cla()
    piexls = receiveMqtt()
    data[i] = piexls
    piexls.resize(8, 8)
    print(str(piexls.max()) + " " + str(piexls.min()) + " " + "温差：" + str(piexls.max() - piexls.min())+"平均："+str(np.mean(piexls)))
    ax.imshow(piexls)
    # ax.imshow(piexls, cmap="gray", vmin=20, vmax=35)
    # ax.imshow(data[i])
    ax.set_title("frame {}".format(i))
    # Note that using time.sleep does *not* work here!
    plt.pause(0.01)
#
# np.save("data01.npy",data)
