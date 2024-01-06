import matplotlib.pyplot as plt
import numpy as np
import time
import os
import Membership_functions as mf
"""
    Run this file for testing and drawing the membership functions (Question 1, part 4)
"""


# GUI Terminal Methods
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


# defining colors for having handsome strings
blue = '\033[94m'
reset = '\033[0m'
red = '\033[91m'
magenta = '\033[95m'
cyan = '\033[96m'

# 1.4
def plot(x,y,name):
    plt.style.use('bmh')

    plt.plot(x, y, color='b', label=name)
    plt.legend()
    plt.show()

# start of the program
if __name__ == "__main__":
    clear_screen()
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
    print(
        blue + "                                                  |________________________________________________________|" + reset)
    print(
        blue + "                                                  | Welcome to our Homemade Membership Function Drawer :)  |")
    print(
        blue + "                                                  |________________________________________________________|" + reset)

    # cleaning the screen
    time.sleep(1)
    clear_screen()

    print(
        cyan + r"                                          \/\/\/\/\/ Please Choose a Membership function to draw \/\/\/\/\/" + reset + '\n')

    print(red + "1. Triangle Membership Function\n")
    print("2. Trap Membership Function" + reset + '\n')

    opt = input(magenta + "Waiting for your Input: " + reset)

    time.sleep(1)
    clear_screen()

    if opt=='1':

        flag = True
        while flag:
            print(
                magenta + "Please Enter a Domain For Triangle Membership Function " + red + "Note: Write it in this format: start[space]end " + reset + '\n')
            d = tuple(map(int, input("Domain: ").split()))
            assert len(d) == 2, red + "Check the format and try again!" + reset
            assert d[0] < d[1], red + "Start was not less than end, please enter the domain again!" + reset
            flag = False

        print("\n" + "_______________________________________________________" + "\n")
        print("Please enter the start, Peak and end point of the Triangle")

        flag = True
        while flag:
            print(
                magenta + "Please enter the start, Peak and end point of the Triangle " + red + "Note: Write it in this format: start[space]peak[space]end " + reset + '\n')
            points = tuple(map(int, input("Domain: ").split()))
            assert len(points) == 3, red + "Check the format and try again!" + reset
            assert points[0] < points[1] < points[2], red + "Check the format and try again!" + reset
            flag = False

        trimmf = mf.trimf_maker(d, points[0], points[1], points[2])

        # X = np.linspace(start=d[0], stop=d[1], num=50)
        X = np.arange(d[0], d[1], 0.1)
        Y = np.array([trimmf(x) for x in X])
        print(Y)

        plot(X, Y, "Triangle Membership Function")





