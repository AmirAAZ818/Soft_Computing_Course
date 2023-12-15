from RGA_Class import RGA
import theorem
import random
from GA_Fuzzy_Controller import Fuzzy_Controller
import numpy as np


def main():
    # # Griewank Function
    # rga_griewank = RGA(target_function=theorem.griewank, fitness_function=lambda x: 370 - theorem.griewank(x),
    #                    function_config=[{'low': -600, 'high': 600}, {'low': -600, 'high': 600},
    #                                     {'low': -600, 'high': 600}, {'low': -600, 'high': 600},{'low': -600, 'high': 600},{'low': -600, 'high': 600}],
    #                    crossover_rate=0.5, max_gen=100, population=80, run_rga=1, controller=Fuzzy_Controller, gpc=5)
    #
    # rga_griewank.Run()

    # Rastrigin Function
    rga_rastrigin = RGA(target_function=theorem.rastrigin, fitness_function=lambda x: 200 - theorem.rastrigin(x),
                        function_config=[{'low': -5.12, 'high': 5.12}, {'low': -5.12, 'high': 5.12},
                                         {'low': -5.12, 'high': 5.12}, {'low': -5.12, 'high': 5.12}],
                        crossover_rate=0.5, max_gen=300, population=300, run_rga=5, controller=Fuzzy_Controller, gpc=20)

    rga_rastrigin.Run()


if __name__ == "__main__":
    main()
