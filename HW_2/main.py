from RGA_Class import RGA
import theorem


def main():
    """
    you can run the algorithm for the function provided and the functions that you want.
    make sure to give the function to the constructor in the required format.
    NOTE: you can Start the algorithm by calling BGA_object.Run() or GA_object.Run()
    WARNING: before using this class install: numpy, tqdm, tabulate, matplotlib
    """

    # Rastrigin Function
    rga_griewank = RGA(target_function=theorem.griewank, fitness_function=lambda x: 250 - theorem.griewank(x),
                       function_config=[{'low': -5.12, 'high': 5.12}, {'low': -5.12, 'high': 5.12},
                                        {'low': -5.12, 'high': 5.12}, {'low': -5.12, 'high': 5.12}],
                       crossover_rate=0.5, mutation_rate=0.01, max_gen=300, population=700, run_rga=30)

    rga_griewank.Run()


if __name__ == "__main__":
    main()
