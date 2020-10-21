# 算法设计
# 开始检测 当前帧温差大于4是表明有人 当前帧为有效帧
# date01 可以完成测试数据检测 单人通过


import matplotlib.pyplot as plt
import numpy as np

data = np.load("data01.npy")

data01 = np.random.random((200, 8, 8))
for i in range(200):
    piexls = data[i]
    piexls.resize(8, 8)
    data01[i] = piexls
    # print("frame:"+str(i)+" 温差："+str(np.max(data01[i]) - np.min(data01[i])))


# print(data01)
# print(np.max(data01[i])-np.min(data01[i]))

def operate(piexls):
    if np.max(piexls) - np.min(piexls) < 4:
        piexls = np.zeros((8, 8))
    else:
        for i in range(8):
            for j in range(8):
                if piexls[i, j] < 23.5:
                    piexls[i, j] = 0
    return piexls


class Frame():
    def __init__(self, piexls):
        # piexls 8x8 np数组
        self.piexls = piexls
        self.pointx, self.pointy = self._point()
        # print(self.pointx)

    def _point(self):
        # 当前帧温度的最高点
        index = int(self.piexls.argmax())
        m, n = self.piexls.shape
        x = int(index / n)
        y = index % n
        return x, y


class Track():
    def __init__(self):
        self.flag = 0
        #  0: error
        # +1:  in
        # -1:  out
        self.pointList = [0]
        # 轨迹行数列表
        self.exist = 0  # 当前处于有效轨迹中
        self.num = 0
        # 室内人数

    def judgeList(self):
        # 判断当前轨迹为进还是出
        list = self.pointList
        if (list[0] == 0 or list[0] == 1) and (list[-1] == 7 or list[-1] == 6):
            self.flag = -1
        elif (list[0] == 7 or list[0] == 6) and (list[-1] == 0 or list[-1] == 1):
            self.flag = 1
        else:
            self.flag = 0
        self.num = self.num + self.flag


T = Track()
# T.pointList
# [1, 2, 5, 6, 7, 6, 7, 6, 7, 7, 7, 0, 2, 3, 4, 5, 6, 6, 7, 7, 7, 6, 7, 7, 6, 4, 3, 2]

fig, ax = plt.subplots()
for i in range(200):
    ax.cla()
    piexls = operate(data01[i])
    F = Frame(piexls)
    if not F.pointy == 0:  # 说明F是有效帧
        T.exist = 1
        T.pointList.append(F.pointx)
    else:
        if T.exist == 1:
            T.judgeList()
            print("frame:" + str(i) + " 人数：" + str(T.num))
        T.exist = 0
        T.pointList = []
    ax.imshow(F.piexls, cmap='gray')
    # ax.imshow(data[i])
    ax.set_title("frame {}".format(i))
    # Note that using time.sleep does *not* work here!
    plt.pause(0.1)

print(T.pointList)
