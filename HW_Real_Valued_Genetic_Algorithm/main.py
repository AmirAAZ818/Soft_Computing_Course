from RGA_Class import RGA
import test_functions


def main():
    """
    you can run the algorithm for the function provided and the functions that you want.
    make sure to give the function to the constructor in the required format.
    NOTE: you can Start the algorithm by calling RGA_object.Run() or RGA_object.Run()
    WARNING: before using this class install: numpy, tqdm, tabulate, matplotlib
    """
    # Griewank Function
    rga_griewank = RGA(target_function=test_functions.griewank, fitness_function=lambda x: 350 - test_functions.griewank(x),
                       function_config=[{'low': -600, 'high': 600}, {'low': -600, 'high': 600},
                                        {'low': -600, 'high': 600}, {'low': -600, 'high': 600}],
                       crossover_rate=0.5, mutation_rate=0.01, max_gen=300, population=700, run_rga=5)

    rga_griewank.Run()


if __name__ == "__main__":
    main()
