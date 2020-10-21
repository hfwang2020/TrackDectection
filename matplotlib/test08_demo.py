# 实时测试
import matplotlib.pyplot as plt
import numpy as np
import paho.mqtt.subscribe as subscribe

np.random.seed(19971111)
data = np.random.random((100000, 64))

data = np.load("data01.npy")

data01 = np.random.random((200, 8, 8))

for i in range(200):
    piexls = data[i]
    piexls.resize(8, 8)
    data01[i] = piexls


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
# ax.imshow(data01[32], vmin=20, vmax=25)
for i in range(200):
    ax.cla()
    piexls = data01[i]
    # piexls = receiveMqtt()
    # data[i] = piexls
    # piexls.resize(8, 8)
    print(str(piexls.max()) + " " + str(piexls.min()) + " " + "温差：" + str(piexls.max() - piexls.min()) + "平均：" + str(
        np.mean(piexls)))
    ax.imshow(piexls, vmin=20, vmax=24)
    # ax.imshow(piexls, cmap="gray", vmin=20, vmax=35)
    # ax.imshow(data[i])
    ax.set_title("frame {}".format(i))
    # Note that using time.sleep does *not* work here!
    plt.pause(0.1)

# np.save("data01.npy",data)
