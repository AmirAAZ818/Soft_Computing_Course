import matplotlib.pyplot as plt
import numpy as np
import time
import os

"""
    Run this file for testing and drawing the membership functions (Question 1, part 4)
"""


# 1.4

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


# defining colors for having handsome strings
blue = '\033[94m'
reset = '\033[0m'
red = '\033[91m'
magenta = '\033[95m'
cyan = '\033[96m'

# start of the program

if __name__ == "__main__":
    clear_screen()
    print("\n\n\n\n\n\n\n\n\n")
    print(blue + "|________________________________________________________|" + reset)
    print(blue + "| Welcome to our Homemade Membership Function Drawer :)  |")
    print(blue + "|________________________________________________________|" + reset)

    # cleaning the screen
    time.sleep(2)
    clear_screen()

    print(cyan + "                                      \/\/\/\/\/ Please Choose a Membership function to draw \/\/\/\/\/" + reset + '\n')

    print(red + "1. Triangle Membership Function")
    print("2. Triangle Membership Function" + reset)

    option = input(magenta + "Waiting for your Input: " + reset)

    time.sleep(2)
    clear_screen()

    print("It was all a lie :)")
