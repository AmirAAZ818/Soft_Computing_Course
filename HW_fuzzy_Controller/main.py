from RGA_Class import RGA
import theorem
import matplotlib.pyplot as plt
import Membership_functions as mfs
import numpy as np


def main():
    # for test
    # low_mf = trapmf_maker([0, 15e-3], 0, [0, 1e-3], 5e-3)
    # avg_mf = trimf_maker([0, 15e-3], 1e-3, 5e-3, 1e-2)
    # high_mf = trapmf_maker([0, 15e-3], 5e-3, [1e-2, 15e-3], 15e-3)
    # x = np.arange(0, 15e-3, 1e-4)
    # y1 = [low_mf(x[i]) for i in range(len(x))]
    # y2 = [avg_mf(x[i]) for i in range(len(x))]
    # y3 = [high_mf(x[i]) for i in range(len(x))]
    #
    #
    # plt.plot(x, y1, color="blue")
    # plt.plot(x, y2, color="green")
    # plt.plot(x, y3, color="red")
    # plt.title('P_m')
    # plt.xlabel('x')
    # plt.ylabel('Degree of Membership')
    # plt.ylim([-0.05, 1.05])
    # plt.show()

    # mf_cm_low = mfs.trapmf_maker([0, float("inf")], 0, [0, 7e-1], 99e-2)
    # mf_cm_high = mfs.trapmf_maker([0, float("inf")], 7e-1, [1, float("inf")], float("inf"))
    # x = np.arange(0, 1.5, 0.1)
    # y1 = [mf_cm_low(x[i]) for i in range(len(x))]
    # y2 = [mf_cm_high(x[i]) for i in range(len(x))]
    # plt.plot(x, y1, color="blue")
    # plt.plot(x, y2, color="green")
    # plt.title('CM')
    # plt.xlabel('x')
    # plt.ylabel('Degree of Membership')
    # plt.ylim([-0.05, 1.05])
    # plt.show()

    mf_gen_low = mfs.trapmf_maker([0, 1], 0, [0, 4e-1], 6e-1)
    mf_gen_mid = mfs.trimf_maker([0,1], 0.4, 0.6, 0.8)
    mf_gen_high = mfs.trapmf_maker([0,1], 6e-1, [8e-1, 1], 1)

    x = np.arange(0, 1.05, 5e-2)
    y1 = [mf_gen_low(x[i]) for i in range(len(x))]
    y2 = [mf_gen_mid(x[i]) for i in range(len(x))]
    y3 = [mf_gen_high(x[i]) for i in range(len(x))]

    plt.plot(x, y1, color="blue")
    plt.plot(x, y2, color="green")
    plt.plot(x, y3, color="red")

    plt.title('GEN')
    plt.xlabel('x')
    plt.ylabel('Degree of Membership')
    plt.ylim([-0.05, 1.05])
    plt.show()



if __name__ == "__main__":
    main()
