import numpy as np


class Track:
    def __init__(self):
        self.flag = 0
        # 轨迹行数列表
        self.pointList = [[0]]
        self.num = 0
        self.diff = 0
        self.empty = 0
        # 室内人数

    def judge(self):
        print("judge running")
        flag = 0
        array = self.pointList
        track_list = []
        if array[1][0] > 7 and array[2][0] > 7:
            flag = -1
        if array[1][0] < 8 and array[2][0] < 8:
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
                        if point <= a+0.5:
                            track_list[-2].append(point)
                        elif point <= b+0.5:
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
                        if point >= a-0.5:
                            track_list[-2].append(point)
                        elif point >= b-0.5:
                            track_list[-1].append(point)
                        else:
                            track_list.append([point])

            count = 0
            for list in track_list:
                if (list[0] < 8) and (list[-1] > 8) and (list.__len__() >= 3):
                    print(list)
                    count += 1
            print("出去", -1 * count * flag, "人")
