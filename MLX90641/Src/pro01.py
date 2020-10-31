# 计算每一列的平均值展示
# 基于"data01.npy" 200farme有人
# mlx90641
# 单人检测v0.2
# 较v0.1加入index权重

import matplotlib.pyplot as plt
import numpy as np
import paho.mqtt.subscribe as subscribe

data01 = np.load("../Dataset/data02.npy")


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
        self.piexls_mean = piexls.mean()
        self.col_mean = self.colmean()
        self.col_media = self.colmedia()
        self.col_diff = self.diff()
        self.index_list = self.points_index()
        self.index = self.indexCal()
        # self.index = self.index_list_to_index()
        # self.index = np.mean(self.index_list)

    def colmean(self):
        piexls = self.piexls
        col_mean = np.ones(16)
        for i in range(16):
            col_mean[i] = piexls[:, i].mean()
        return col_mean

    def colmedia(self):
        piexls = self.piexls
        col_media = np.ones(16)
        for i in range(16):
            col_media[i] = np.median(piexls[:, i])
            # col_media[i] = piexls[:, i].median()
        return col_media

    def diff(self):
        col = self.col_mean
        # col = self.col_media
        col_diff = np.ones(16)
        col_diff[0] = abs(4 * col[0] - col[1] - col[2] - 2 * self.piexls_mean)
        col_diff[1] = abs(4 * col[1] - col[2] - col[3] - 2 * self.piexls_mean)
        col_diff[14] = abs(4 * col[14] - col[12] - col[13] - 2 * self.piexls_mean)
        col_diff[15] = abs(4 * col[15] - col[14] - col[13] - 2 * self.piexls_mean)
        for i in range(2, 14):
            col_diff[i] = abs(4 * col[i % 16] - col[(i + 1) % 16] - col[(i - 1) % 16] - col[(i + 2) % 16] - col[
                (i - 2) % 16])
        # col_diff[0] = 0
        # col_diff[-1] = 0
        return col_diff

    # 可以改进的地方加入list里面值的权重
    def points_index(self):
        col = self.col_diff
        index_list = []
        # 列表极大点和差值大于2的点列坐标 -> 异常点
        for i in range(2, 14):
            # if ((col[i] > col[i - 1] and col[i] > col[i + 1]) and (col[i] > 2)):
            if col[i] > 2:
                index_list.append(i)
        return index_list
        # 当前帧无异常点，返回 -1

    def index_list_to_index(self):
        index_list = self.index_list
        index = -1
        if index_list.__len__() == 0:
            index = -1
        else:
            index = np.mean(index_list)
        # 双人算法优化index
        # elif index_list.__len__() == 3:
        #     if abs(index_list[0] - index_list[-1]) <= 5:
        #         index = np.mean(index_list)
        # else:
        #     index = np.mean(index_list)
        return index

    def indexCal(self):
        col_list = self.col_diff
        index = -1
        # print(col_list)
        if max(col_list) <= 4:
            return index
        col = 0
        sum1 = 0
        sum2 = 0
        for i in col_list:
            sum2 += i
            sum1 += col * i
            col += 1
        index = sum1 / sum2
        return round(index, 2)


class Track():
    def __init__(self):
        self.flag = 0
        #  0: error
        # +1:  in
        # -1:  out
        self.pointList = [0]
        # 轨迹行数列表
        self.num = 0
        self.diff = 0
        # 室内人数

    def judge(self):
        list = self.pointList
        diff = self.diff
        # 每两帧之间的diff
        piexls_diff = list[-1] - list[-2]

        if piexls_diff > 10:
            piexls_diff = 0
        # 7,7,7,7,7 -> 1,2,1,1,2,2,
        if (list[-2] > 5 and list[-2] < 10) and (list[-1] > 11 or list[-1] < 4):
            a = list[-1]
            list = [0, a]
        if list.__len__() >= 3:
            diff += piexls_diff
        if diff > 7:
            diff = 0
            self.flag = 1
            list = [0]
            self.num += self.flag
            print("diff: ", diff, "进1人", self.num)
        elif diff < -7:
            diff = 0
            self.flag = -1
            list = [0]
            self.num += self.flag
            print("diff: ", diff, "出1人", self.num)
        self.diff = diff
        self.pointList = list
        print(list)

T = Track()

fig, ax = plt.subplots()
col = np.ones(16)
for i in range(0, 10000):
    ax.cla()
    piexls = data01[i]
    # piexls = receiveMqtt()
    # piexls.resize(12, 16)
    F = Frame(piexls)
    if F.index > 0:
        if not (F.index == T.pointList[-1]):
            T.pointList.append(F.index)
            T.judge()
            print(T.pointList, "\t", "diff: ", T.diff)

    col = F.col_diff
    col_img = col.copy()
    col_img.resize(1, 16)
    # ax.imshow(col_img, vmin=20, vmax=30)
    ax.imshow(col_img, vmin=2, vmax=5)
    # ax.imshow(piexls, cmap="gray", vmin=20, vmax=35)
    # ax.imshow(data[i])
    ax.set_title("frame {}".format(i))
    # Note that using time.sleep does *not* work here!
    plt.pause(0.1)
#
# np.save("data01.npy",data)
