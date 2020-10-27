import numpy as np

# a = np.zeros((3,2,2))
#
# a[1]=np.array([[1,1],[2,2]])
#
# print(a)

a = np.random.random((8,8))

m, n = a.shape
index = int(a.argmax())
x = int(index / n)
y = index % n
print(x, y)