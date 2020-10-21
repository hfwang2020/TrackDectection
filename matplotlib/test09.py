# 算法设计 v0.3
# 思路 改变amg8833安装位置
# 检测当前帧的平均温度 高于平均帧数的点个数 判断有无人
#
# 致命缺点：从外面冷环境进来的人几乎无温差 顾无法判断

import paho.mqtt.subscribe as subscribe
import matplotlib.pyplot as plt
import numpy as np
import time

data = np.load("data01.npy")


def receiveMqtt():
    msg = subscribe.simple("test", hostname="192.168.1.120")
    msg = str(msg.payload)
    msg_list = msg.split(sep=",")
    msg_list = msg_list[1:65]
    piexls = []
    for i in msg_list:
        piexls.append(float(i))
    piexls1 = np.array(piexls)
    piexls1.resize(8, 8)
    return piexls1


data01 = np.random.random((200, 8, 8))

for i in range(200):
    piexls = data[i]
    piexls.resize(8, 8)
    data01[i] = piexls


# print("frame:"+str(i)+" 温差："+str(np.max(data01[i]) - np.min(data01[i])))


# print(data01)
# print(np.max(data01[i])-np.min(data01[i]))

def operate(piexls):
    # piexls 8x8
    # 温差小于4的帧全部置0 且 小于23.5的点也置0
    # if np.max(piexls) - np.min(piexls) < 3.5:
    #     piexls = np.zeros((8, 8))
    # else:
    #     for i in range(8):
    #         for j in range(8):
    #             if piexls[i, j] < (piexls.min()+piexls.max())/2:
    #                 piexls[i, j] = 0
    return piexls


class Frame():
    def __init__(self, piexls):
        # piexls 8x8 np数组
        self.piexls = piexls
        self.pointx, self.pointy = self._point()
        # 当前帧的平均温度
        self.piexls_mean = np.mean(piexls)
        # 温度大于平均值的点的个数
        self.high_points, self.high_points_index_sum = self.highcal()
        # print(self.pointx)
        self.high_points_index = 0
        if (self.high_points > 1):
            self.high_points_index = self.high_points_index_sum / self.high_points

    def _point(self):
        # 当前帧温度的最高点
        index = int(self.piexls.argmax())
        m, n = self.piexls.shape
        x = int(index / n)
        y = index % n
        return x, y

    def highcal(self):
        num = 0
        sumofIndex = 0
        for i in range(8):
            for j in range(8):
                if piexls[i][j] > self.piexls_mean + 2:
                    num = num + 1;
                    # j 列 i 行
                    sumofIndex = sumofIndex + j;

        return num, sumofIndex


class Track():
    def __init__(self):
        self.flag = 0
        #  0: error
        # +1:  in
        # -1:  out
        self.pointList = [0]
        # 轨迹行数列表
        self.exist = 0  # 当前处于有效轨迹中
        self.num = 8
        # 室内人数

    def judgeList(self):
        # 判断当前轨迹为进还是出
        list = self.pointList
        print(list)
        # if (list[0] == 0 or list[0] == 1 or list[0] == 2) and (list[-1] == 7 or list[-1] == 6 or list[-1] == 5) and (
        #         3 in list or 4 in list):
        #     self.flag = 1
        # elif (list[0] == 7 or list[0] == 6 or list[0] == 5) and (list[-1] == 0 or list[-1] == 1 or list[-1] == 2) and (
        #         3 in list or 4 in list):
        #     self.flag = -1
        # else:
        #     self.flag = 0
        if list.__len__() == 1:
            self.flag = 0
        elif ((list[0] < 3) or (list[1] < 3)) and ((list[-1] > 5) or (list[-2] > 5)):
            self.flag = -1
        elif ((list[0] > 5) or (list[1] > 5)) and ((list[-1] < 3) or (list[-2] < 3)):
            self.flag = 1
        else:
            self.flag = 0

        self.num = self.num + self.flag
        self.flag = 0


T = Track()
# T.pointList
# [1, 2, 5, 6, 7, 6, 7, 6, 7, 7, 7, 0, 2, 3, 4, 5, 6, 6, 7, 7, 7, 6, 7, 7, 6, 4, 3, 2]

fig, ax = plt.subplots()
for i in range(200000):
    ax.cla()
    # time.sleep(0.05)
    piexls = operate(receiveMqtt())
    # piexls = data01[i]
    F = Frame(piexls)
    print("Frame:", i, "highpoint:  ", F.high_points, "index: ", F.high_points_index)
    if F.high_points > 1:  # 说明F是有效帧
        T.exist = 1
        T.pointList.append(F.high_points_index)
    else:
        if T.exist == 1:
            T.judgeList()
            print("frame:" + str(i) + "    人数：" + str(T.num))
        T.exist = 0
        T.pointList = []

    ax.imshow(F.piexls,cmap="gray")
    ax.imshow(F.piexls)
    ax.set_title("frame {}".format(i))
    # Note that using time.sleep does *not* work here!
    plt.pause(0.05)


# print(T.pointList)
