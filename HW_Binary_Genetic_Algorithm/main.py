from BGA_Class import BGA
import theorem


def main():
    """
    you can run the algorithm for the function provided and the functions that you want.
    make sure to give the function to the constructor in the required format.
    NOTE: you can Start the algorithm by calling BGA_object.Run() or GA_object.Run()
    WARNING: before using this class install: numpy, tqdm, tabulate, matplotlib
    """

    # Rastrigin function
    rast_bga = BGA(target_function=theorem.rastrigin, function_dim=4, population=600, crossover_rate=0.8,
                   mutation_rate=0.005, max_gen=350, error=0.001,
                   function_config=[{'low': -5.12, 'high': 5.12}, {'low': -5.12, 'high': 5.12},
                                    {'low': -5.12, 'high': 5.12}, {'low': -5.12, 'high': 5.12}],
                   fitness_function=lambda x: 85 - theorem.rastrigin(x), run_bga=30,
                   plot_dir=r"E:\University of Kerman\Term 5\Soft Computing\HomeWorks\Soft_Computing_Course\HW_1\Plots")

    rast_bga.Run()

    # Griewank Function
    grie_bga = BGA(target_function=theorem.griewank, function_dim=4, population=1000, crossover_rate=0.85,
                   mutation_rate=0.005, max_gen=400, error=0.001,
                   function_config=[{'low': -600, 'high': 600}, {'low': -600, 'high': 600},
                                    {'low': -600, 'high': 600}, {'low': -600, 'high': 600}],
                   fitness_function=lambda x: 250 - theorem.griewank(x), run_bga=5,
                   plot_dir=r"E:\University of Kerman\Term 5\Soft Computing\HomeWorks\Soft_Computing_Course\HW_1\Plots")

    grie_bga.Run()


if __name__ == "__main__":
    main()
