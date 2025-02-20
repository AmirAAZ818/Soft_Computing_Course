from GSA_Class import GSA
import test_functions


def main():
    """
    you can run the algorithm for the function provided and the functions that you want.
    make sure to give the function to the constructor in the required format.
    NOTE: you can Start the algorithm by calling GSA_object.Run() or GSA_object.Run()
    WARNING: before using this class install: numpy, tqdm, tabulate, matplotlib
    """
    # Griewank Function
    gsa_griewank = GSA(function=test_functions.griewank, domain=[{'low': -600, 'high': 600}, {'low': -600, 'high': 600},
                                                                 {'low': -600, 'high': 600},
                                                                 {'low': -600, 'high': 600}], function_dim=4,
                       pop_size=300,
                       ittration=100, k=10, G=2.4, a=1, runs=1)

    gsa_griewank.run()


if __name__ == "__main__":
    main()
