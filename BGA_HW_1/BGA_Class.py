from random import randint, random


# class for BGA Algo

class BGA:
    def __init__(self, target_function, function_dim, population,
                 crossover_rate, mutation_rate, chromosome_bits=8):

        self.population_matrix = None
        self.function = target_function  # تابع هدف
        self.parameters = function_dim  # تعداد پارامترهای تابع
        self.population = population  # اندازه جمعیت
        self.chromosome_len = chromosome_bits
        self.pc = crossover_rate
        self.pm = mutation_rate

    # For making random population
    def Random_Chromosome(self):
        population_matrix = []  # N x Sigma(Li) from i = 0 to function_dim

        for i in range(self.population):
            chromosome = []
            for j in range(self.chromosome_len):
                chromosome.append(randint(0, 1))
            population_matrix.append(chromosome)

        self.population_matrix = population_matrix

    
    def Mutation(self, child_matrix):
        rand = random()
        if rand > self.pm:
            return
        else:
            i = randint(0, self.population - 1)
            j = randint(0, self.chromosome_len - 1)
            child_matrix[i, j] = not child_matrix[i, j]
            return

    def Get_Fitness_Value(self, fitfunct, choro):
        return fitfunct(choro)


def main():
    # just for testing
    bga1 = BGA(target_function=lambda x: x ** 2, function_dim=2, population=10, crossover_rate=0.8, mutation_rate=0.2,
               chromosome_bits=8)
    bga1.Random_Chromosome()
    print(bga1.population_matrix)


if __name__ == "__main__":
    main()
