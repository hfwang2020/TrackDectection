import numpy as np


data01 = np.load("/home/hfwang/Desktop/DeV/VsCoDe/TrackDectection/MLX90641/Dataset/data03.npy")

a = data01[154]
b = [0]*16

f = open("/home/hfwang/Desktop/DeV/VsCoDe/TrackDectection/MLX90641/Test/out.txt","w")

for p in range(500):
    a = data01[p]
    for i in range(16):
        b[i] = round(np.var(a[:,i]),2)
    print("frame:",p,file=f)
    print(b,file=f)


