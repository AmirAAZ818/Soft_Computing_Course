from RGA_Class import RGA
import theorem
import matplotlib.pyplot as plt
from Membership_functions import trimf_maker, trapmf_maker
import numpy as np

def main():
    # for test
    mf1 = trimf_maker([0, 10], 2, 5, 8)
    mf2 = trapmf_maker([0,float("inf")], 0,[0,10], 10)
    x = np.arange(0, 20, 1)
    Y = [mf2(x[i]) for i in range(len(x))]


    plt.plot(x, Y)
    plt.title('trimf')
    plt.xlabel('x')
    plt.ylabel('Degree of Membership')
    # plt.ylim([-0.05, 1.05])
    plt.show()

if __name__ == "__main__":
    main()
