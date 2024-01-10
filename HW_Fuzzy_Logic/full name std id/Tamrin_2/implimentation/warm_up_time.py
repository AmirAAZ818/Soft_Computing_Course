import numpy as np
import skfuzzy as fuzz
from matplotlib import pyplot as plt

start = 0
stop = 90
step = 1
x = np.arange(start, stop, step)

# Triangular membership function
trimf_1 = fuzz.trimf(x, [ 0, 0, 23])
trimf_2 = fuzz.trimf(x, [0, 23, 45])
trimf_3 = fuzz.trimf(x, [23, 45, 67])
trimf_4 = fuzz.trimf(x, [45, 67, 89])
trimf_5 = fuzz.trimf(x, [67, 89, 89])


plt.xlabel("warm up time")
plt.ylabel("Mebership")
plt.plot(x, trimf_1, label="Too Short")
plt.plot(x, trimf_2, label="Short")
plt.plot(x, trimf_3, label="Medium")
plt.plot(x, trimf_4, label="Long")
plt.plot(x, trimf_5, label="Too Long")
plt.legend(loc="upper right")
plt.show()