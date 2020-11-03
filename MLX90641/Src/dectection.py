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
data01 = np.load("../Dataset/data03.npy")

# print(data01.shape)

T = Track()
debug_index_list = []
fig, ax = plt.subplots()
fig1, bx = plt.subplots()

col = np.ones(16)
for i in range(150, 500):
    ax.cla()
    bx.cla()
    piexls = data01[i]
    # piexls = receiveMqtt()
    # piexls.resize(12, 16)
    F = Frame(piexls)
    if F.index > 0:
        if not (F.index == T.pointList[-1]):
            debug_index_list.append(F.index)
            T.pointList.append(F.index)
            T.judge()
            # print(T.pointList, "\t", "diff: ", T.diff)

    col = F.col_var
    col_img = col.copy()
    col_img.resize(1, 16)

    ax.imshow(col_img, vmin=0.3, vmax=0.8)
    bx.imshow(piexls)

    print("frame", i, F.index_list)
    # ax.imshow(piexls, cmap="gray", vmin=20, vmax=35)
    ax.set_title("frame {}".format(i))
    bx.set_title("piexls {}".format(i))
    plt.pause(0.5)

print(debug_index_list)
