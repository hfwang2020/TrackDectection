import matplotlib.pyplot as plt
import numpy as np


data = np.load("data01.npy")



# data01 = np.random.random((200,8,8))
# for i in range(200):
#     piexls = data[i]
#     piexls.resize(8, 8)
#     data01[i]=piexls
#
# print(data01)

data01 = data

# for i in range(200):
#     for j in range(64):
#         if data01[i,j]<23.5:
#             data01[i,j]=0




fig, ax = plt.subplots()

for i in range(200):
    ax.cla()
    piexls = data01[i]
    piexls.resize(8, 8)
    print(str(piexls.max()) + " " + str(piexls.min()) + " " + "温差：" + str(piexls.max() - piexls.min()))

    ax.imshow(piexls,cmap='gray')
    # ax.imshow(data[i])
    ax.set_title("frame {}".format(i))
    # Note that using time.sleep does *not* work here!
    plt.pause(0.1)

