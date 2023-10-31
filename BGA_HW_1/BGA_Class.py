from random import randint, random
import theorem
import math
import matplotlib.pyplot as plt


class BGA:

    def __init__(self, max_gen, target_function, fitness_function, function_dim, population,
                 crossover_rate, mutation_rate, precision, function_config):

        self.func_config = function_config  # a list of dicts containing boundary of each dimension : [{"low": a, "high":b}, ...]
        self.population_matrix = None
        self.function = target_function  # تابع هدف
        self.fit_func = fitness_function  # the fitness function
        self.dim = function_dim  # تعداد پارامترهای تابع
        self.population = population  # اندازه جمعیت
        self.chromosome_len = 0
        self.pc = crossover_rate
        self.pm = mutation_rate
        self.max_gen = max_gen  # maximum number of generations
        self.last_gen = 0
        self.precision = precision  # quantization error
        self.L = [0 for i in range(self.dim)]
        self.history = {"avg_fitness": [], "best_so_far": []}

    def Run(self):
        print("BGA Is Running .....")
        # print("_________Parameters_________")


        self.get_len_chro()  # estimating the number of bits for each dimension.
        self.Random_population()  # Making random population
        # debug
        print("Random Population Matrix is __________")
        print(self.population_matrix)
        print("L is _______")
        print(self.L)

        for generation in range(self.max_gen):
            print(f"________________ Generation : {generation} ________________")
            self.one_gen()

        print("________Plotting________")
        self.plot_info()



    def one_gen(self):

        decoded_population = self.decode_chromosomes()
        fitness_values = self.get_Fitness(decoded_chromosomes=decoded_population)
        self.log(fitness_values)
        mating_pool = self.roulette_wheel(fitness_values)
        next_gen_v1 = self.Crossover(mating_pool)
        nex_gen = self.Mutation(next_gen_v1)
        print(f"new gen is : {nex_gen}")
        self.population_matrix = nex_gen
        self.last_gen += 1






    def roulette_wheel(self,
                       fitness_values):  # inputs fitness values of each chromosome, returns the mating pool Matrix of size N x L
        sum_fitness = sum(fitness_values)
        probs = [(fitness / sum_fitness) for fitness in fitness_values]

        prob = 0
        cumulative_probs = [0 for i in range(self.population)]

        for i in range(len(probs)):
            prob += probs[i]
            cumulative_probs[i] = prob

        # Selecting N chromosomes from population matrix
        mating_pool = []
        for i in range(self.population):
            r_num = random()
            idx = 0

            for j in range(len(cumulative_probs)):
                if cumulative_probs[j] > r_num:
                    idx = j
                    break

            mating_pool.append(self.population_matrix[idx])

        return mating_pool

    def log(self, fitness_list):  # saves the best so far and avg fitness to log
        self.history["best_so_far"].append(max(fitness_list))
        self.history["avg_fitness"].append(sum(fitness_list) / len(fitness_list))

    def Random_population(self):
        population_matrix = []  # N x Sigma(Li) from i = 0 to function_dim

        for i in range(self.population):
            chromosome = []
            for j in range(self.chromosome_len):
                chromosome.append(randint(0, 1))
            population_matrix.append(chromosome)

        self.population_matrix = population_matrix

    def get_len_chro(
            self):  # a method that values the length list: L. where L[i] means the length of the bits used for the i'th variable.

        # private method
        def var_bit_len(boundary,
                        idx):  # boundary is a dictionary : bound = {"low": a, "high": b}, output : appending the bit len of the corresponding variable in the L list
            # we use precision and its formula to estimate bit len of the variable
            rng = boundary['high'] - boundary['low']
            length = math.ceil(math.log(rng / self.precision, 2) - 1)
            # print()
            self.L[idx] = length

        boundaries = self.func_config  # giving the config to a variable called boundaries
        for var_idx in range(len(boundaries)):  # giving each boundary to the method we made and updating the L list
            var_bit_len(boundaries[var_idx], var_idx)

        self.chromosome_len = sum(self.L)

    def decode_chromosomes(self):  # returns a tuple of tuples of the decoded value for variables, size: N x dim
        def binary_to_decimal(
                binary_num):  # binary_num is a list of 0s and 1s. we join it and make it string, and then we convert it using a special way in python
            b_num = list(map(str, binary_num))
            return int(''.join(b_num), 2)

        def decode_chromosome(
                chromosome):  # returns a tuple containing the real values of the genes for a given chromosome
            rng = 0
            decoded_chromosome = []
            for gene_idx, length in enumerate(self.L):
                # print(f"________________________bit len of L_{gene_idx} is : {length}_____________________________")
                # converting from binary to decimal
                # print("$$$$$$$$$$$Binary to decimal phase$$$$$$$$$$$$")
                new_rng = rng + length

                x_i = chromosome[rng:new_rng]  # slice of the list that contains the gene bits
                # print(f"sliced chromosome : {x_i}")
                decoded_gene = binary_to_decimal(x_i)  # decoded_gene = decoded binary number
                # print(f"decimal converted gene  : {decoded_gene}")

                # normalizing the decoded gene value
                # print("$$$$$$$ Normalizing phase $$$$$$$$")
                no_decoded_gene = decoded_gene / ((2 ** length) - 1)
                # print(f"normalized gene : {no_decoded_gene}")

                # next step (don't know it in english :) )
                # print("$$$$$$$$$$ Negasht phase $$$$$$$")
                config = self.func_config[gene_idx]  # assigning the boundary of the gene to a variable called config
                # print(f"dim config is : {config}")
                x_real = config["low"] + ((config['high'] - config['low']) * no_decoded_gene)
                # print(f"x real is : {x_real}")
                decoded_chromosome.append(x_real)

                rng = new_rng

            return tuple(decoded_chromosome)

        # giving each chromosome to the decode_chromosome function and adding it in a list
        decoded_values = []  # this will be converted to a tuple at the end
        for chro in self.population_matrix:
            # print("_________________________________________________")
            # print(f"Current chromosome is : {chro}")
            decoded_values.append(decode_chromosome(chro))

        return tuple(decoded_values)

    def Crossover(self, mating_pool_mat):  # input: selected choros for parents / output: a matrix of childs
        # this function gets parent matrix(selected parents for making child)
        # and after cross over returns child matrix
        child_matrix = []
        i = 0
        while i < self.population - 1:
            if random() > self.pc:
                child_matrix.append(mating_pool_mat[i])
                child_matrix.append(mating_pool_mat[i + 1])
                i += 2
            else:
                point = randint(0, self.chromosome_len)
                # print(point)
                child1 = mating_pool_mat[i]
                child2 = mating_pool_mat[i + 1]
                for j in range(point, self.chromosome_len):
                    child2[j] = mating_pool_mat[i][j]
                    child1[j] = mating_pool_mat[i + 1][j]

                child_matrix.append(child1)
                child_matrix.append(child2)
                i += 2

        return child_matrix


    def Mutation(self, child_matrix):  # input: a matrix of childs from cross over stage / output: mutated child_matrix
        # this function gets a matrix of childs, this matrix is output of cross over stage
        # if rand is less than pm, changes 1 bit of one random choromosom 
        mutation_mat = [[1 if random() <= self.pm else 0 for i in range(self.chromosome_len)] for j in range(self.population)]
        mutated_matrix = [[bit1 ^ bit2 for bit1, bit2 in zip(mutation_mat[i], child_matrix[i])] for i in range(self.population)]

        return mutated_matrix

    def get_Fitness(self,
                    decoded_chromosomes):  # returns a tuple of size N(population), that represents the fitness value for each chromosome
        fitness_values = [0 for i in range(self.population)]

        for i in range(len(decoded_chromosomes)):
            chromosome = decoded_chromosomes[i]
            fitness_values[i] = self.fit_func(chromosome)

        return tuple(fitness_values)

    def plot_info(self):

        fig, axis = plt.subplots(1, 2)

        # Plot of avg fitness
        y = self.history['avg_fitness']
        x = list(range(self.max_gen))
        axis[0].plot(x, y, label="Average Fitness", color="blue")

        # Plot of the best fitness so far
        y = self.history['best_so_far']
        x = list(range(self.max_gen))
        axis[1].plot(x, y, label="Best So Far", color="blue")
        plt.legend()
        plt.show()
        # plt.savefig(r"E:\University of Kerman\Term 5\Soft Computing\HomeWorks\Soft_Computing_Course\BGA_HW_1\Plots\BGA_plots.png")




def main():
    # just for testing
    bga1 = BGA(target_function=theorem.fGriewank, function_dim=2, population=200, crossover_rate=0.8,
               mutation_rate=0.1, max_gen=200, precision=0.01,
               function_config=[{'low': -600, 'high': 600}, {'low': -600, 'high': 600}],
               fitness_function=theorem.fGriewank)



    # print(bga1.population_matrix)
    #
    bga1.Run()
    #
    # print(bga1.population_matrix)
    # print(bga1.L)
    # print(bga1.chromosome_len)
    # bga1.get_len_chro()
    # bga1.Random_population()
    # print(bga1.population_matrix)
    # print('-----------------------')
    # bga1.Crossover(bga1.population_matrix)
    # print(bga1.Child_matrix)
    # print('-----------------')
    # bga1.Mutation(bga1.Child_matrix)
    # print(bga1.Child_matrix)
    # mutation_mat = [[1 if random() <= 0.2 else 0 for i in range(10)] for j in
    #                 range(6)]
    # child_matrix = [[randint(0, 1) for i in range(10)] for j in range(6)]
    # mutated_matrix = [[bit1 ^ bit2 for bit1, bit2 in zip(mutation_mat[i], child_matrix[i])] for i in
    #                   range(6)]
    # print(mutation_mat)
    # print(child_matrix)
    # print(mutated_matrix)



if __name__ == "__main__":
    main()
