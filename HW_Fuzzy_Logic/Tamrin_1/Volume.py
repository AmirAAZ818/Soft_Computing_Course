import numpy as np
import skfuzzy as fuzz
from matplotlib import pyplot as plt

start = 0
stop = 1000
step = 1
x = np.arange(start, stop, step)


trimf_1 = fuzz.trimf(x, [ 0, 0, 500])
trimf_2 = fuzz.trimf(x, [ 0, 500, 1000])
trimf_3 = fuzz.trimf(x, [ 500, 1000, 1000])

plt.xlabel("volume")
plt.ylabel("Mebership")
plt.plot(x, trimf_1, label="little")
plt.plot(x, trimf_2, label="mediuum")
plt.plot(x, trimf_3, label="big")
plt.legend(loc="upper right")
plt.show()