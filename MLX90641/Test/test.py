# # import numpy as np
#
#
# # data01 = np.load("/home/hfwang/Desktop/DeV/VsCoDe/TrackDectection/MLX90641/Dataset/data03.npy")
#
# # a = data01[154]
# # b = [0]*16
#
# # f = open("/home/hfwang/Desktop/DeV/VsCoDe/TrackDectection/MLX90641/Test/out.txt","w")
#
# # for p in range(500):
# #     a = data01[p]
# #     for i in range(16):
# #         b[i] = round(np.var(a[:,i]),2)
# #     print("frame:",p,file=f)
# #     print(b,file=f)
#
# import numpy as np
#
# col_list = [-1,1,-1,-1,-1,-1,1,1,2,-1,-1,-1,-1,-1,-1,-1]
# index = []
#
# # for i in range(16):
# #     print(i)
# #     if col_list[i] > 0:
# #         temp = 0
# #         while(col_list[i] > 0):
# #             temp += col_list[i]
# #             i += 1
# #         index.append(temp)
# i = 0
# temp = 0
# index = []
# while(i<16):
#     if col_list[i]>0:
#         temp = 0
#         while(col_list[i]>0 and i<16):
#             temp+=col_list[i]
#             i += 1
#         index.append(temp)
#     i += 1
#
#
# print(index)

import numpy as np

pointList = [
    [14],
    [13],
    [12, 14],
    [10, 13],
    [7, 10],
    [3, 5],

]

flag = 0
array = pointList
track_list = []
if (array[1][0] > 7) and (array[2][0] > 7):
    flag = -1
if (array[1][0] < 8) and (array[2][0] < 8):
    flag = 1
# flag = -1

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
            if point <= a:
                track_list[-2].append(point)
            elif point <= b:
                track_list[-1].append(point)
            else:
                track_list.append([point])



# flag = 1
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
            if point >= a:
                track_list[-2].append(point)
            elif point >= b:
                track_list[-1].append(point)
            else:
                track_list.append([point])

print(track_list)
