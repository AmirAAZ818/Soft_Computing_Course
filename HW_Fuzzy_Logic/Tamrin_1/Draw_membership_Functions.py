import matplotlib.pyplot as plt
import numpy as np
import time
import os
import Membership_functions as mf
from random import random, uniform, randint

"""
    Run this file for testing and drawing the membership functions (Question 1, part 4)
"""


# GUI Terminal Methods
def clear_screen(sleep=1):
    time.sleep(sleep)
    os.system('cls' if os.name == 'nt' else 'clear')


# defining colors for having handsome strings
blue = '\033[94m'
reset = '\033[0m'
red = '\033[91m'
magenta = '\033[95m'
cyan = '\033[96m'


# Question 1
def plot(x, y, name):

    plt.plot(x, y, color='b', label=name)
    plt.title(name)
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
    clear_screen()

    print(
        cyan + r"                                          \/\/\/\/\/ Please Choose a Membership function to draw \/\/\/\/\/" + reset + '\n')

    print(red + "1. Asked Membership Function (Question 1)\n")
    print("2. Triangle Membership Function\n")
    print("3. Trapezoid Membership Function" + reset + '\n')

    opt = input(magenta + "Waiting for your Input: " + reset)

    # cleaning the screen
    clear_screen()

    # Setting style of the plots
    plt.style.use('bmh')


    if opt == '1':

        # Deciding the mode of Plotting (Random Plotting or Getting l and r from user and plotting it)
        print(red + "1. User plotting Mode" + "\n")
        print("2. Computer Plotting Mode" + reset + '\n')

        u_mode = False
        c_mode = False

        inp = input("Choose: ")

        if inp == '1':
            u_mode = True
        elif inp == '2':
            c_mode = True
        else:
            print(red + "There is only two modes available" + reset)

            # cleaning the screen
            clear_screen()
        if u_mode:
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
            # %%%%%%%%%%%%%%%%%%%%%%%%%%%%%    1.1    %%%%%%%%%%%%%%%%%%%%%%%%%%%%%
            curvemf = mf.Q1mf_maker(l=l, r=r)
            X = np.linspace(start=l - 10, stop=r + 10, num=int(l - r + 50))
            Y = np.array([curvemf(x) for x in X])
            plot(X, Y, "Question 1 Membership Function")


        # %%%%%%%%%%%%%%%%%%%%%%%%%%%%%    1.2    %%%%%%%%%%%%%%%%%%%%%%%%%%%%%
        # Plotting the Membership Function
        elif c_mode:
            # init figure
            fig, axs = plt.subplots(2, 3, figsize=(10, 6))

            # ploting each function with random r and l
            num = 1
            for i in range(2):
                for j in range(3):
                    # Generating l and r
                    l = round(randint(0, 30) - random(), 3)
                    r = round(l + randint(1, 30) + random(), 3)

                    # Making the membership function
                    curvemf = mf.Q1mf_maker(l=l, r=r)
                    X = np.linspace(start=l - 10, stop=r + 10, num=int(l - r + 50))
                    Y = np.array([curvemf(x) for x in X])

                    # Plotting
                    axs[i, j].plot(X, Y, color='r')
                    axs[i, j].set_title(f'Plot Num. {num}')
                    axs[i, j].text(0.95, 0.95, f"r = {r}" + "\n" + f"l = {l}", transform=axs[i, j].transAxes, fontsize=10, color='blue', ha='right', va='top')

                    num += 1

            plt.tight_layout()
            plt.show()

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
