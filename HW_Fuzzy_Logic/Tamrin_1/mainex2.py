from ex2 import *

def get_inputs():
    t = int(input('degree: '))
    v = int(input('volume: '))
    c = int(input('C: '))
    return Fuzzy_food_control(temp=t, vol=v, tc=c)

def main():
    food = get_inputs()
    food.run()


main()