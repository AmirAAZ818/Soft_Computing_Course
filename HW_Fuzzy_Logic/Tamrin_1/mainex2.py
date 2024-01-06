from ex2 import *

def get_inputs():
    t = input('degree: ')
    v = input('volume: ')
    c = input('C: ')
    return Fuzzy_food_control(temp=t, vol=v, tc=c)

def main():
    food = get_inputs()
    food.run()

if __name__ == '__main__':
    main()