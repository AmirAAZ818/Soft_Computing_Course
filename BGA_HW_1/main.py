from BGA_Class import BGA
import theorem

def main():
    """
    you can run the algorithm for the function provided and the functions that you want.
    make sure to give the function to the constructor in the required format.
    NOTE: you can Start the algorithm by calling BGA_object.Run() or GA_object.Run()
    """

    # mccormick function
    mcc_bga = BGA(target_function=theorem.mccormick, function_dim=2, population=500, crossover_rate=0.8,
               mutation_rate=0.005, max_gen=80, error=0.001,
               function_config=[{'low': -1.5, 'high': 4}, {'low': -3, 'high': 4}],
               fitness_function=lambda x: 45 - theorem.mccormick(x), run_bga=5)

    # mcc_bga.Run()








if __name__ == "__main__":
    main()