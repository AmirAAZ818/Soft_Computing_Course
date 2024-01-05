import numpy as np
import skfuzzy as fuzz
from matplotlib import pyplot as plt

start = 0
stop = 100
step = 1
x = np.arange(start, stop, step)

# Triangular membership function
trimf_1 = fuzz.trimf(x, [ 0, 0, 50])
trimf_2 = fuzz.trimf(x, [ 0, 50, 100])
trimf_3 = fuzz.trimf(x, [ 50, 100, 100])


plt.xlabel("Degree")
plt.ylabel("Mebership")
plt.plot(x, trimf_1, label="low")
plt.plot(x, trimf_2, label=("average"))
plt.plot(x, trimf_3, label="high")
plt.legend(loc="upper right")
plt.show()