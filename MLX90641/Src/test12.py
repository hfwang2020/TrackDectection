# 计算每一列的平均值展示
# 基于"data01.npy" 200farme有人
# mlx90641
import matplotlib.pyplot as plt
import numpy as np
import paho.mqtt.subscribe as subscribe

np.random.seed(19971111)
data = np.random.random((100000, 64))
data01 = np.load("../Dataset/data01.npy")


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


class Frame():
    def __init__(self, piexls):
        # piexls 12x16 np数组
        self.piexls = piexls
        self.col = self.colcal()

    def colcal(self):
        piexls = self.piexls
        col = np.zeros((2, 16))
        for i in range(16):
            col[:, i] = piexls[:, i].mean()


class Track():
    def __init__(self):
        self.flag = 0
        #  0: error
        # +1:  in
        # -1:  out
        self.pointList = [0]
        # 轨迹行数列表
        self.exist = 0  # 当前处于有效轨迹中
        self.num = 5
        # 室内人数


fig, ax = plt.subplots()
col = np.zeros((2, 16))
for i in range(100000):
    ax.cla()
    piexls = data01[i]
    # piexls = receiveMqtt()
    # piexls.resize(12, 16)
    for a in range(16):
        col[:, a] = piexls[:, a].mean()
    ax.imshow(col, vmin=20, vmax=30)
    # ax.imshow(piexls, cmap="gray", vmin=20, vmax=35)
    # ax.imshow(data[i])
    ax.set_title("frame {}".format(i))
    # Note that using time.sleep does *not* work here!
    plt.pause(0.01)
#
# np.save("data01.npy",data)
