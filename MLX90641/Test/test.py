# import numpy as np


# data01 = np.load("/home/hfwang/Desktop/DeV/VsCoDe/TrackDectection/MLX90641/Dataset/data03.npy")

# a = data01[154]
# b = [0]*16

# f = open("/home/hfwang/Desktop/DeV/VsCoDe/TrackDectection/MLX90641/Test/out.txt","w")

# for p in range(500):
#     a = data01[p]
#     for i in range(16):
#         b[i] = round(np.var(a[:,i]),2)
#     print("frame:",p,file=f)
#     print(b,file=f)

import numpy as np

col_list = [-1,1,-1,-1,-1,-1,1,1,2,-1,-1,-1,-1,-1,-1,-1]
index = []

# for i in range(16):
#     print(i)
#     if col_list[i] > 0:
#         temp = 0
#         while(col_list[i] > 0):
#             temp += col_list[i]
#             i += 1
#         index.append(temp)
i = 0
temp = 0
index = []
while(i<16):
    if col_list[i]>0:
        temp = 0
        while(col_list[i]>0 and i<16):
            temp+=col_list[i]
            i += 1
        index.append(temp)
    i += 1


print(index)
