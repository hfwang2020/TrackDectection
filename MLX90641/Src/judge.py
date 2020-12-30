import numpy as np
import paho.mqtt.subscribe as subscribe

data01 = np.load("../Dataset/data06.npy")


class Track:
    def __init__(self):
        # 轨迹进出的标志
        self.flag = 0
        # 轨迹行数列表
        self.pointList = [[0]]
        self.num = 0
        # 空闲时间
        self.time = 0

    #
    def judge(self):
        print("judge running")
        flag = 0
        array = self.pointList
        track_list = []
        if array[1][0] > 7:
            flag = -1
        if array[1][0] < 7:
            flag = 1
        # flag = -1
        # 14 -> 0
        if flag == -1:
            for i in range(array.__len__()):
                for point in array[i]:
                    if track_list.__len__() == 0:
                        track_list.append([point])
                    elif track_list.__len__() == 1:
                        if point > track_list[0][-1]:
                            track_list.append([point])
                        else:
                            track_list[0].append(point)
                    else:
                        a = track_list[-2][-1]
                        b = track_list[-1][-1]
                        if point <= a + 0.5:
                            track_list[-2].append(point)
                        elif point <= b + 0.5:
                            track_list[-1].append(point)
                        else:
                            track_list.append([point])

            count = 0
            for list in track_list:
                if (list[0] > 8) and (list[-1] < 8) and (list.__len__() >= 3):
                    print(list)
                    count += 1
            print("进来", -1 * count * flag, "人")
        # 0 -> 14
        if flag == 1:
            for i in range(array.__len__()):
                for point in array[i]:
                    if track_list.__len__() == 0:
                        track_list.append([point])
                    elif track_list.__len__() == 1:
                        if point < track_list[0][-1]:
                            track_list.append([point])
                        else:
                            track_list[0].append(point)
                    else:
                        a = track_list[-2][-1]
                        b = track_list[-1][-1]
                        if point >= a - 0.5:
                            track_list[-2].append(point)
                        elif point >= b - 0.5:
                            track_list[-1].append(point)
                        else:
                            track_list.append([point])

            count = 0
            for list in track_list:
                if (list[0] < 8) and (list[-1] > 8) and (list.__len__() >= 3):
                    print(list)
                    count += 1
            print("出去", -1 * count * flag, "人")


class Frame:
    def __init__(self, piexls):
        # piexls 12x16 np数组
        # col_mean、col_diff、col_var、col_final都是 1x16 np数组
        self.piexls = piexls
        self.mean = float(np.mean(piexls))
        # col_mean 列平均值
        self.col_mean = self.colmean()
        # col_diff 列与全帧温度平均值的差
        self.col_diff = self.colCal_1()
        # 列方差 一般方差小于1的列无人
        self.col_var = self.colCal_2()
        # col_mean 和 col_diff 加权成最终判断的依据col
        self.col_final = self.col_diff.copy() + self.col_var.copy()
        # index_list 是有人点的坐标 无人的帧index_list是[-1]
        # 例
        # [1 , 13]
        self.index_list = self.indexCal_3()
        # 有人点的平均值 负值则无人
        self.index = np.mean(self.index_list)

    def colmean(self):
        piexls = self.piexls
        col_mean = np.ones(16)
        for i in range(16):
            col_mean[i] = np.mean(piexls[:, i])
        return col_mean

    # col_diff 列平均值与全帧平均值的差
    def colCal_1(self):
        piexls_mean = self.mean
        col_mean = self.col_mean
        col = np.ones(16)
        for i in range(16):
            col[i] = 4 * (col_mean[i] - piexls_mean)
        return col

    # debug2 算方差
    def colCal_2(self):
        piexls1 = self.piexls
        b = np.ones(16)
        for i in range(16):
            b[i] = round(10 * np.var(piexls1[:, i]), 2)
        return b

    def indexCal_3(self):
        col_list = self.col_final.copy()
        # index 是当前帧有人点的列坐标列表
        index = []
        count_above_1 = 0
        for i in range(16):
            # 列值小于8的点置-1 为无人点
            if col_list[i] >= 8:
                count_above_1 += 1
            else:
                col_list[i] = -1
        if count_above_1 <= 1:
            return [-1]
        i = 0
        # 遍历col 找到连续的两个有人点算出位置
        while i < 16:
            if col_list[i] < 0:
                i = i + 1
                continue
            track_point = 0
            sum_i = 0
            sum_col_i = 0
            while i < 16 and col_list[i] > 0:
                track_point = track_point + 1
                sum_i += col_list[i]
                sum_col_i += i * col_list[i]
                i = i + 1
            if track_point > 1 and 12 > sum_col_i / sum_i > 2:
                index.append(round((sum_col_i / sum_i), 2))
        if index.__len__() == 0:
            return [-1]
        else:
            return index


T = Track()

for i in range(100000):
    piexls = data01[i]
    F = Frame(piexls)
    # index 大于0 说明有人

    if F.index > 0:
        # 清空time
        T.time = 0
        # 当此时有人列坐标列表跟上一帧不一样时往T.pointList里面插入index_list

        if not (F.index_list == T.pointList[-1]):
            T.pointList.append(F.index_list)
            print("frame", i, F.index_list)
    else:
        # 无人循环次数加1
        T.time += 1

    # 空闲循环数大于20 对Track里面的ponitlist进行一次判断
    if (T.time >= 20) and (T.pointList.__len__() >= 3):
        T.judge()
        T.pointList = [[]]
        T.time = 0
    # 输出无人
    if (T.time >= 100) and (T.pointList.__len__() <= 2):
        T.pointList = [[]]
        print(".....clear.....")
        T.time = 0
