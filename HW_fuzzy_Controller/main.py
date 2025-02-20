from RGA_Class import RGA
import test_functions
from GA_Fuzzy_Controller import Fuzzy_Controller


def main():
    # Rastrigin Function
    rga_rastrigin = RGA(target_function=test_functions.rastrigin, fitness_function=lambda x: 200 - test_functions.rastrigin(x),
                        function_config=[{'low': -5.12, 'high': 5.12}, {'low': -5.12, 'high': 5.12},
                                         {'low': -5.12, 'high': 5.12}, {'low': -5.12, 'high': 5.12}],
                        crossover_rate=0.5, max_gen=300, population=300, run_rga=5, controller=Fuzzy_Controller, gpc=20)

    rga_rastrigin.Run()




if __name__ == "__main__":
    main()
