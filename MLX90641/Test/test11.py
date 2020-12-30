# 测试data01.npy
# mlx90641
import matplotlib.pyplot as plt
import Frame
import numpy as np
import paho.mqtt.subscribe as subscribe
from utils import *

np.random.seed(19971111)
data = np.random.random((100000, 64))
data01 = np.load("../Dataset/data06.npy")




fig, ax = plt.subplots()
# fig, bx = plt.subplots()
# 300 jia come in
# 1300-1400 in

for i in range(1300, 1550):
    ax.cla()
    # bx.cla()
    piexls_past = data01[i-1]
    piexls_now = data01[i]
    piexls = (piexls_now - piexls_past)+2

    # F = Frame(piexls)
    # piexls = receiveMqtt()
    # piexls.resize(12, 16)
    # print(piexls.max()," ",piexls.min()," ","温差：",piexls.max() - piexls.min(),"平均：",np.mean(piexls))
    ax.imshow(piexls,vmin=2.5,vmax=4)
    # col = F.col_diff
    # col_img = col.copy()
    # col_img.resize(1, 16)
    # ax.imshow(col_img, vmin=20, vmax=30)
    # bx.imshow(col_img, vmin=2, vmax=5)
    # ax.imshow(piexls, cmap="gray", vmin=20, vmax=35)
    # ax.imshow(data[i])
    ax.set_title("frame {}".format(i))
    # bx.set_title("frame {}".format(i))
    # Note that using time.sleep does *not* work here!
    plt.pause(0.01)
