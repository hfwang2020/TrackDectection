import numpy as np


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
        # print(list)