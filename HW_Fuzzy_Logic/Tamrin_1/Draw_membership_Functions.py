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
def plot(x, y, name):
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

    print(red + "1. Asked Membership Function (Question 1)\n")
    print("2. Triangle Membership Function\n")
    print("3. Trapezoid Membership Function" + reset + '\n')

    opt = input(magenta + "Waiting for your Input: " + reset)

    time.sleep(1)
    clear_screen()

    if opt == '1':

        print(magenta + "Please Enter l and r For the Asked Membership Function")

        flag = True
        while flag:
            print('\n' + red + "Note: Write it in this format: l[space]r " + reset + '\n')
            args = tuple(map(float, input("Type: ").split()))
            l, r = args
            if len(args) != 2:
                print(red + "Check the Format and Try Again!" + reset)
                continue

            if l >= r:
                print(red + "l and r are not written in the right order" + reset)
            flag = False    

        # -------------------- The Actual code you may want to check --------------------
        mf = mf.Q1mf_maker(l=l, r=r)

        X = np.linspace(start=l - 10, stop=r + 10, num=int(l - r + 50))
        Y = np.array([mf(x) for x in X])

        plot(X, Y, "Question 1 Membership Function")
        # -------------------- End of he Actual code you may want to check --------------------


    # Triangle Drawing Option
    elif opt == '2':

        print(magenta + "Please Enter a Domain For Triangle Membership Function ")

        flag = True
        while flag:

            print('\n' + red + "Note: Write it in this format: Start[space]End " + reset + '\n')
            d = tuple(map(float, input("Type: ").split()))

            if len(d) != 2:
                print(red + "Check the Format and Try Again!" + reset)
                continue

            if d[0] > d[1]:
                print(red + "Start was not less than End, please enter the domain again!" + reset)
                continue

            flag = False

        print("\n" + "_______________________________________________________" + "\n")
        print("Please enter the Start, Peak and End point of the Triangle")

        flag = True
        while flag:
            print('\n' + red + "Note: Write it in this format: start[space]peak[space]end " + reset + '\n')
            points = tuple(map(float, input("Type: ").split()))
            if (d[0] > points[0]) or (d[1] < points[2]):
                print(red + "Start or End are not in the domain, check your values!")
                continue

            if len(points) != 3:
                print(red + "Check the Format and Try Again!" + reset)
                continue

            if (points[0] > points[1]) or (points[1] > points[2]):
                print(red + "Values are not in order" + reset)
                continue

            flag = False

        # -------------------- The Actual code you may want to check --------------------
        trimmf = mf.trimf_maker(d, points[0], points[1], points[2])

        X = np.linspace(start=d[0], stop=d[1], num=100)
        Y = np.array([trimmf(x) for x in X])

        plot(X, Y, "Triangle Membership Function")
        # -------------------- End of he Actual code you may want to check --------------------

        # Trapezoid Drawing Option
    elif opt == '3':

        print(magenta + "Please Enter a Domain For Trapezoid Membership Function ")
        flag = True
        while flag:

            print('\n' + red + "Note: Write it in this format: Start[space]End " + reset + '\n')
            d = tuple(map(float, input("Type: ").split()))

            if len(d) != 2:
                print(red + "Check the Format and Try Again!" + reset)
                continue

            if d[0] > d[1]:
                print(red + "Start was not less than End, please enter the domain again!" + reset)
                continue

            flag = False

        print("\n" + "_______________________________________________________" + "\n")
        print("Please enter the Start, Peak and End point of the Membership Fucntion")

        flag = True
        while flag:
            print(
                '\n' + red + "Note: Write it in this format: Start[space]Peak_start[space]Peak_end[space]End " + reset + '\n')
            points = tuple(map(float, input("Type: ").split()))
            if (d[0] > points[0]) or (d[1] < points[3]):
                print(red + "Start or End are not in the domain, check your values!")
                continue

            if len(points) != 4:
                print(red + "Check the Format and Try Again!" + reset)
                continue

            if (points[0] > points[1]) or (points[1] > points[2]) or (points[2] > points[3]):
                print(red + "Values are not in order" + reset)
                continue

            flag = False

        # -------------------- The Actual code you may want to check --------------------
        trapmf = mf.trapmf_maker(d, points[0], (points[1], points[2]), points[3])

        X = np.linspace(start=d[0], stop=d[1], num=100)
        Y = np.array([trapmf(x) for x in X])

        plot(X, Y, "Trapezoid Membership Function")
        # -------------------- End of he Actual code you may want to check --------------------
