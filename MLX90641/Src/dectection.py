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
data01 = np.load("../Dataset/data06.npy")

# print(data01.shape)

T = Track()
debug_index_list = []

# fig, ax = plt.subplots()
# fig1, bx = plt.subplots()

col = np.ones(16)
i = 1300

while (i<1500):
    i += 1
    # ax.cla()
    # bx.cla()
    piexls = data01[i]

    # piexls = receiveMqtt()
    # piexls.resize((12, 16))

    F = Frame(piexls)
    if F.index > 0:
        T.empty = 0
        # 当此时有人列坐标列表跟上一帧不一样时往T.pointList里面插入index_list
        #
        if not (F.index_list == T.pointList[-1]):
            T.pointList.append(F.index_list)
            print("frame", i, F.index_list)
    else:
        T.empty += 1

    if (T.empty >= 20) and (T.pointList.__len__() >= 3):
        T.judge()
        T.pointList = [[]]
        T.empty = 0
    if (T.empty >= 100) and (T.pointList.__len__() <= 2):
        T.pointList = [[]]
        print(".....clear.....")
        T.empty = 0
