from BGA_Class import BGA
import theorem

def main():
    # mccormick function
    bga1 = BGA(target_function=theorem.mccormick, function_dim=2, population=500, crossover_rate=0.8,
               mutation_rate=0.005, max_gen=80, error=0.001,
               function_config=[{'low': -1.5, 'high': 4}, {'low': -3, 'high': 4}],
               fitness_function=lambda x: 45 - theorem.mccormick(x), run_bga=5)

    







if __name__ == "__main__":
    main()