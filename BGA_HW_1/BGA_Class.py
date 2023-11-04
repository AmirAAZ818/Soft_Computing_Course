from random import randint, random
import theorem
import math
import matplotlib.pyplot as plt
from tqdm import tqdm, trange
from tabulate import tabulate


class BGA:

    def __init__(self, target_function, fitness_function, function_dim, population,
                 crossover_rate, mutation_rate, error, function_config, max_gen=50, run_bga=30):

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
        self.error = error  # quantization error
        self.L = [0 for i in range(self.dim)]
        self.history = {"mean_fitness": [], "best_so_far": [], "avg_mean_fitness": [], "avg_best_so_far": []}
        self.best_so_far = {'fitness': 0, "chromosome": list()}
        self.best_current = {'fitness': 0, "chromosome": list()}
        self.runs = run_bga
        self.best_answers = []  # best decoded value of the chromosomes found in each full run of the algorithm

    def print_parameters(self):
        # This is a method that prints parameters in tabular structure
        parameters = [
            ["Algorithm Runs", self.runs],
            ["Maximum Generation", self.max_gen],
            ["Population Size", self.population],
            ["Error", self.error],
            ["CrossOver Rate", self.pc],
            ["Mutation Rate", self.pm],
            ["Chromosome Length", self.chromosome_len],
            ["Input Bit Length", self.L],
            ["Function Input Shape", self.dim]
        ]
        print(tabulate(parameters, headers=["Parameter", "Value"], tablefmt="fancy_grid"))

    def Run(self):
        # Starting the algo
        print("\033[1;36;40m" + "=" * 50)
        print("\033[1;36;40m" + "   Running Binary Genetic Algorithm   ")
        print("\033[1;36;40m" + "=" * 50 + "\033[0m")

        # First step
        self.get_len_chro()  # estimating the number of bits for each dimension.

        # printing the params in tabular structure
        self.print_parameters()

        print("______________________________________")

        for run in range(self.runs):
            # Reset the properties that were given values for one fully run of the algorithm
            self.reset()

            # Fully running the algorithm
            print(f"Run : {run + 1}")
            self.one_run()

            # Logging lists of best_so_far and mean fitness produced by one_run().
            self.log_algo()

        solution, opt = self.post_process()
        # Showing results
        print("________________________ Results ________________________")
        print(f"Average Best Solution     :        {solution}")
        print(f"Optimum Value             :        {opt}")
        print(f"Last Average Best So Far  :        {self.history['avg_best_so_far'][self.last_gen - 1]}")
        print(f"Last Average Mean Fitness :        {self.history['avg_mean_fitness'][self.last_gen - 1]}")

        # Plotting absf, amf
        self.plot_info()

    def post_process(self):
        """This method processes self.history['avg_mean_fitness'] and self.history['avg_best_so_far'] and self.best_answers'}
        returns:
            1. Mean Best Solution (mean of the best answers found in each run)
            2. Optimum value found for the target function
        """

        # Evaluating best solution
        mean_best_solutions = [0 for i in range(self.dim)]

        for i in range(self.dim):
            _sum = 0
            for j in range(self.runs):
                _sum += self.best_answers[j][i]

            mean_best_solutions[i] = _sum / len(self.best_answers)

        # avg best so far, and avg mean fitness
        avg_mean_fitness = [0 for i in range(self.max_gen)]
        avg_best_so_far = [0 for i in range(self.max_gen)]

        for i in range(self.max_gen):
            for j in range(self.runs):
                avg_mean_fitness[i] += self.history['avg_mean_fitness'][j][i]
                avg_best_so_far[i] += self.history['avg_best_so_far'][j][i]
            avg_mean_fitness[i] = avg_mean_fitness[i] / self.runs
            avg_best_so_far[i] = avg_best_so_far[i] / self.runs

        self.history['avg_mean_fitness'] = avg_mean_fitness
        self.history['avg_best_so_far'] = avg_best_so_far

        # Optimum found
        opt = self.function(mean_best_solutions)

        return tuple(mean_best_solutions), opt

    def reset(self):
        """This method empties the lists and values
        used for tracking the metrics for one fully run of the algorithm"""

        self.history['mean_fitness'] = []
        self.history['best_so_far'] = []

        self.best_so_far['fitness'] = 0
        self.best_so_far['chromosome'] = []

        self.best_current['fitness'] = 0
        self.best_current['chromosome'] = []

        self.last_gen = 0

    def one_run(self):  # This method fully runs the algorithm once
        self.Random_population()  # Making random population

        # running the algorithm
        for generation in trange(self.max_gen):
            self.one_gen()

        # Saving fitness values of the last produced population
        decoded_population = self.decode_chromosomes()
        fitness_values = self.get_Fitness(decoded_chromosomes=decoded_population)
        self.log_gen(fitness_values)

    def one_gen(self):  # This method produces one generation of the algorithm

        decoded_population = self.decode_chromosomes()
        fitness_values = self.get_Fitness(decoded_chromosomes=decoded_population)
        self.log_gen(fitness_values)  # log the info of the last generation
        mating_pool = self.roulette_wheel(fitness_values)
        next_gen_v1 = self.Crossover(mating_pool)
        nex_gen = self.Mutation(next_gen_v1)
        # print(f"Population : {nex_gen}")
        self.population_matrix = nex_gen
        self.last_gen += 1

    def roulette_wheel(self,
                       fitness_values):
        """inputs fitness values of each chromosome, returns the mating pool Matrix of size N x L"""
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

    def log_gen(self, fitness_list):
        """saves the best so far and avg fitness of a generation in one run of BGA"""

        # updating best so far property
        if self.best_so_far['fitness'] < max(fitness_list):
            self.best_so_far['fitness'] = max(fitness_list)
            self.best_so_far['chromosome'] = self.population_matrix[fitness_list.index(self.best_so_far['fitness'])]

        # updating the best current property
        self.best_current['fitness'] = max(fitness_list)
        self.best_current['chromosome'] = self.population_matrix[fitness_list.index(self.best_current['fitness'])]

        # Saving history
        self.history["best_so_far"].append(self.best_so_far['fitness'])
        self.history["mean_fitness"].append(sum(fitness_list) / len(fitness_list))

    def log_algo(self):
        self.history["avg_mean_fitness"].append(self.history['mean_fitness'])
        self.history["avg_best_so_far"].append(self.history['best_so_far'])

        # Saving the best decoded value of the chromosome of the last generated population
        decoded_best_last_chromosome = self.decode_chromosome(chromosome=self.best_current['chromosome'])
        self.best_answers.append(decoded_best_last_chromosome)

    def Random_population(self):
        population_matrix = []  # N x Sigma(Li) from i = 0 to function_dim

        for i in range(self.population):
            chromosome = []
            for j in range(self.chromosome_len):
                chromosome.append(randint(0, 1))
            population_matrix.append(chromosome)

        self.population_matrix = population_matrix

    def get_len_chro(
            self):
        """a method that values the length list: L.
        where L[i] means the length of the bits used for the i'th variable."""

        # private method
        def var_bit_len(boundary,
                        idx):
            """boundary is a dictionary : bound = {"low": a, "high": b},
            output : appending the bit len of the corresponding variable in the L list"""

            # we use error and its formula to estimate bit len of the variable
            rng = boundary['high'] - boundary['low']
            length = math.ceil(math.log(rng / self.error, 2) - 1)
            self.L[idx] = length

        boundaries = self.func_config  # giving the config to a variable called boundaries
        for var_idx in range(len(boundaries)):  # giving each boundary to the method we made and updating the L list
            var_bit_len(boundaries[var_idx], var_idx)

        self.chromosome_len = sum(self.L)

    def decode_chromosome(self,  # A method for decoding a chromosome
                          chromosome):  # returns a tuple containing the real values of the genes for a given chromosome

        def binary_to_decimal(
                binary_num):
            """binary_num is a list of 0s and 1s.
            we join it and make it string, and then we convert it using a special way in python"""

            b_num = list(map(str, binary_num))
            return int(''.join(b_num), 2)

        rng = 0
        decoded_chromosome = []
        for gene_idx, length in enumerate(self.L):
            new_rng = rng + length

            x_i = chromosome[rng:new_rng]  # slice of the list that contains the gene bits
            decoded_gene = binary_to_decimal(x_i)  # decoded_gene = decoded binary number

            # normalizing the decoded gene value
            no_decoded_gene = decoded_gene / ((2 ** length) - 1)

            # next step (don't know it in english :) )
            config = self.func_config[gene_idx]  # assigning the boundary of the gene to a variable called config
            x_real = config["low"] + ((config['high'] - config['low']) * no_decoded_gene)
            decoded_chromosome.append(x_real)

            rng = new_rng

        return tuple(decoded_chromosome)

    def decode_chromosomes(self):
        """returns a tuple of tuples of the decoded value for variables, size: N x dim
        # giving each chromosome to the decode_chromosome function and adding it in a list """

        decoded_values = []  # this will be converted to a tuple at the end
        for chro in self.population_matrix:
            # print("_________________________________________________")
            # print(f"Current chromosome is : {chro}")
            decoded_values.append(self.decode_chromosome(chro))

        return tuple(decoded_values)

    def Crossover(self, mating_pool_mat):
        """input: selected choros for parents / output: a matrix of children
        this function gets parent matrix (selected parents for making child)
        and after cross over returns child matrix """

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

    def Mutation(self, child_matrix):
        """ input: a matrix of children from cross over stage / output: mutated child_matrix
        this function gets a matrix of children, this matrix is output of cross over stage
        if rand is less than pm, changes one bit of one random chromosome """
        mutation_mat = [[1 if random() <= self.pm else 0 for i in range(self.chromosome_len)] for j in
                        range(self.population)]
        mutated_matrix = [[bit1 ^ bit2 for bit1, bit2 in zip(mutation_mat[i], child_matrix[i])] for i in
                          range(self.population)]

        return mutated_matrix

    def get_Fitness(self,
                    decoded_chromosomes):
        """returns a tuple of size N(population),
        that represents the fitness value for each chromosome"""

        fitness_values = [0 for i in range(self.population)]

        for i in range(len(decoded_chromosomes)):
            chromosome = decoded_chromosomes[i]
            fitness_values[i] = self.fit_func(chromosome)
        return tuple(fitness_values)

    def plot_info(self):

        plt.style.use('Solarize_Light2')

        # Plot of avg fitness
        y2 = self.history['avg_best_so_far']
        y1 = self.history['avg_mean_fitness']
        x = list(range(self.max_gen))

        plt.plot(x, y1, label="Average Mean Fitness", color="blue")
        plt.plot(x, y2, label="Average Best So Far", color="red", ls="--")

        plt.legend()
        plt.show()
        # plt.savefig(r"E:\University of Kerman\Term 5\Soft Computing\HomeWorks\Soft_Computing_Course\BGA_HW_1\Plots\BGA_plots.png")