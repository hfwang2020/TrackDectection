# 计算每一列的平均值展示
# 基于"data01.npy" 200farme有人
# mlx90641 12x16 8hz
# 单人检测v0.2
# 较v0.1加入index权重
# idea:利用方差判断人

import matplotlib.pyplot as plt
import numpy as np
import paho.mqtt.subscribe as subscribe
import matplotlib
from Track import Track
from Frame import Frame
from utils import *

matplotlib.use('TkAgg')

# data01 = np.load("/home/hfwang/Desktop/DeV/VsCoDe/TrackDectection/MLX90641/Dataset/data03.npy")
# data01 = np.load("../Dataset/data03.npy")

# print(data01.shape)

T = Track()
debug_index_list = []
# fig, ax = plt.subplots()
# fig1, bx = plt.subplots()

col = np.ones(16)
for i in range(0, 20000000):

    # ax.cla()
    # bx.cla()

    # piexls = data01[i]

    piexls = receiveMqtt()
    piexls.resize((12, 16))

    F = Frame(piexls)
    if F.index > 0:
        T.empty = 0
        if not (F.index_list == T.pointList[-1]):
            T.pointList.append(F.index_list)
            print("frame", i, F.index_list)

        # print(T.pointList, "\t", "diff: ", T.diff)
    else:
        # print(T.empty)
        T.empty += 1

    if (T.empty >= 10) and (T.pointList.__len__() >= 3):
        T.judge()
        T.pointList = [[]]
        T.empty = 0

    col = F.col_final
    col_img = col.copy()
    col_img.resize(1, 16)

    # ax.imshow(col_img, vmin=5, vmax=10)
    # bx.imshow(piexls)

    # ax.set_title("frame {}".format(i))
    # bx.set_title("piexls {}".format(i))
    plt.pause(0.01)

print(debug_index_list)
