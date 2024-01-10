from HW_Fuzzy_Logic.Tamrin_2.fuzzy_food_control import *

def get_inputs():
    t = int(input('degree: '))
    v = int(input('volume: '))
    c = int(input('C: '))
    return Fuzzy_food_control(temp=t, vol=v, tc=c)

def main():
    food = get_inputs()
    food.run()

if __name__ == '__main__':
    main()