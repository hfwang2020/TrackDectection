import numpy as np

a = np.random.random((500, 12, 16))

b = np.ones((12, 16))

col = np.zeros((2, 16))

for i in range(16):
    col[:, i] = b[:, i].mean()

print(b)
print(col)
