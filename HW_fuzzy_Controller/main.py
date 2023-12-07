from RGA_Class import RGA
import theorem
import random
from GA_Fuzzy_Controller import Fuzzy_Controller

def main():
    # Griewank Function
    rga_griewank = RGA(target_function=theorem.griewank, fitness_function=lambda x: 370 - theorem.griewank(x),
                       function_config=[{'low': -600, 'high': 600}, {'low': -600, 'high': 600},
                                        {'low': -600, 'high': 600}, {'low': -600, 'high': 600}],
                       crossover_rate=0.5, max_gen=300, population=700, run_rga=1, controller=Fuzzy_Controller, gpc=30)

    rga_griewank.Run()








if __name__ == "__main__":
    main()
