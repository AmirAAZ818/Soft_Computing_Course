import numpy as np

X = np.linspace(start=10, stop=30, num=50)
print(X)
idx = np.where(X == 25)
print(idx[0])
print(np.size(idx[0]))
