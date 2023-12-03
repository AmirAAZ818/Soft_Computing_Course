from RGA_Class import RGA
import theorem
import matplotlib.pyplot as plt
from Membership_functions import trimf_maker, trapmf_maker
import numpy as np


def main():
    # for test
    low_mf = trapmf_maker([0, 15e-3], 0, [0, 1e-3], 5e-3)
    avg_mf = trimf_maker([0, 15e-3], 1e-3, 5e-3, 1e-2)
    high_mf = trapmf_maker([0, 15e-3], 5e-3, [1e-2, 15e-3], 15e-3)
    x = np.arange(0, 15e-3, 1e-4)
    y1 = [low_mf(x[i]) for i in range(len(x))]
    y2 = [avg_mf(x[i]) for i in range(len(x))]
    y3 = [high_mf(x[i]) for i in range(len(x))]

    plt.plot(x, y1, color="blue")
    plt.plot(x, y2, color="green")
    plt.plot(x, y3, color="red")
    plt.title('P_m')
    plt.xlabel('x')
    plt.ylabel('Degree of Membership')
    plt.ylim([-0.05, 1.05])
    plt.show()


if __name__ == "__main__":
    main()
