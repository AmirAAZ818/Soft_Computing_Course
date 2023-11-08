from random import randint, random, uniform, gauss
import math
import matplotlib.pyplot as plt
from tqdm import tqdm, trange
from tabulate import tabulate
import os


class RGA:

    def __init__(self, target_function, fitness_function, function_dim, population,
                 crossover_rate, mutation_rate, error, function_config, plot_dir, max_gen=50, run_bga=30):

        self.func_config = function_config  # a list of dicts containing boundary of each dimension : [{"low": a, "high":b}, ...]
        self.population_matrix = None
        self.function = target_function  # تابع هدف
        self.fit_func = fitness_function  # the fitness function
        self.dim = function_dim  # تعداد پارامترهای تابع
        self.population = population  # اندازه جمعیت
        self.pc = crossover_rate
        self.pm = mutation_rate
        self.max_gen = max_gen  # maximum number of generations
        self.last_gen = 0
        self.error = error  # quantization error
        self.history = {"mean_fitness": [], "best_so_far": [], "avg_mean_fitness": [], "avg_best_so_far": []}
        self.best_so_far = {'fitness': 0, "chromosome": list()}
        self.best_current = {'fitness': 0, "chromosome": list()}
        self.runs = run_bga
        self.best_answers = []  # best decoded value of the chromosomes found in each full run of the algorithm
        self.save_dir = plot_dir

    def print_parameters(self):
        # This is a method that prints parameters in tabular structure
        parameters = [
            ["Algorithm Runs", self.runs],
            ["Maximum Generation", self.max_gen],
            ["Population Size", self.population],
            ["Error", self.error],
            ["CrossOver Rate", self.pc],
            ["Mutation Rate", self.pm],
            ["Chromosome Length", self.dim],
            ["Function Input Shape", self.dim]
        ]
        print(tabulate(parameters, headers=["Parameter", "Value"], tablefmt="fancy_grid"))

    def Run(self):
        # Starting the algo
        print("\033[1;36;40m" + "=" * 50)
        print("\033[1;36;40m" + "   Running Real Genetic Algorithm   ")
        print("\033[1;36;40m" + "=" * 50 + "\033[0m")

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
        fitness_values = self.get_Fitness(chromosomes=decoded_population)
        self.log_gen(fitness_values)

    def one_gen(self):
        """This method produces one generation of the algorithm"""

        fitness_values = self.get_Fitness(chromosomes=self.population_matrix)

        self.log_gen(fitness_values)  # log the info of the last generation
        mating_pool = self.roulette_wheel(fitness_values)
        next_gen_v1 = self.Crossover(mating_pool)
        nex_gen = self.Mutation(next_gen_v1)
        self.population_matrix = nex_gen
        self.last_gen += 1

    def roulette_wheel(self,
                       fitness_values):
        """inputs fitness values of each chromosome
        return: Mating pool Matrix of size N x dim"""
        sum_fitness = sum(fitness_values)
        probs = [(fitness / sum_fitness) for fitness in fitness_values]

        prob = 0
        cumulative_probs = [0 for i in range(self.population)]

        for i in range(len(probs)):
            prob += probs[i]
            cumulative_probs[i] = prob

        # Selecting N chromosomes from population matrix
        mating_pool = []  # A matrix of size N x dim

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
        """saves the best so far and avg fitness of a generation in one run of RGA"""

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
        """
        This method randomly init a population matrix with continuous uniform distribution
        """

        population_matrix = []  # N x d Matrix

        for i in range(self.population):
            chromosome = [0 for k in range(self.dim)]
            for j in range(self.dim):
                l_bound = self.func_config[j]['low']
                h_bound = self.func_config[j]['high']
                chromosome[j] = (uniform(0, 1) * (h_bound - l_bound)) + l_bound
            population_matrix.append(chromosome)

        self.population_matrix = population_matrix

    def Crossover(self, mating_pool_mat):
        """input: selected choros for parents / output: a matrix of children
        this function gets parent matrix (selected parents for making child)
        and after cross over returns child matrix """

        def clip_vector(vector):
            """
            This method clips the values of the vector with respect to high bound and low bound of the vector

            :return: Clipped vector(list)
            """
            return [max(min(vector[i], self.func_config[i]['high']), self.func_config[i]['low']) for i in
                    range(self.dim)]

        def vmult(value, vector):
            """
            This method multiplies value in each element of the list and returns it
            :param value: value you want to multiply in a vector
            :param vector: you know what it is :)
            :return: value * vector
            """
            return [value * element for element in vector]

        def vadd(v1, v2):
            """
            This method adds v1 and v2 elementwise and returns a list v3
            :param v1: vector 1
            :param v2: vector 2
            :return: v1 + v2 (list of len(v1))
            """
            assert len(v1) == len(v2)

            return [e1 + e2 for e1, e2 in zip(v1, v2)]

        landa1 = uniform(0, 1)
        landa2 = 1 - landa1

        child_matrix = []
        i = 0
        while i < self.population - 1:
            if random() > self.pc:
                child_matrix.append(mating_pool_mat[i])
                child_matrix.append(mating_pool_mat[i + 1])
                i += 2
            else:
                # generating landas for each crossover

                parent1 = mating_pool_mat[i]
                parent2 = mating_pool_mat[i + 1]

                child1 = vadd(vmult(landa1, parent1), vmult(landa2, parent2))
                child2 = vadd(vmult(landa2, parent1), vmult(landa1, parent2))

                child_matrix.append(child1)
                child_matrix.append(child2)
                i += 2

        return child_matrix

    def Mutation(self, child_matrix):
        """
        This method applies Mutation phase on Child Matrix

        :return: next generation, a matrix of size N x dim
        """
        for i in range(self.population):
            if random() < self.pm:
                # Perform mutation on each gene of the chromosome
                for j in range(self.dim):
                    l_bound = self.func_config[j]['low']
                    h_bound = self.func_config[j]['high']
                    mutation_mean = (h_bound + l_bound) / 2
                    mutation_std = (h_bound - l_bound) / 4  # Mutation Standard # todo
                    mutation_value = gauss(mu=mutation_mean, sigma=mutation_std)
                    mutation_value = max(min(mutation_value, h_bound),
                                         l_bound)  # Clip the value to be within the bounds
                    child_matrix[i][j] = mutation_value

        return child_matrix

    def get_Fitness(self, chromosomes):
        """returns a tuple of size N(population),
        that represents the fitness value for each chromosome"""

        fitness_values = [0 for i in range(self.population)]

        for i in range(len(chromosomes)):
            chromosome = chromosomes[i]
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
        # plt.show()
        plt.savefig(os.path.join(self.save_dir, "BGA_plot.png"))


def f(x, y):
    x = y


def main():
    # testing random population method
    rga = RGA(f, f, 2, 4, 0.8, 0.005, 0.01, [{'low': 1, 'high': 2}, {'low': 1, 'high': 2}],
              '~/Documents/GitHub/Soft_Computing_Course')

    rga.Random_population()
    print(rga.population_matrix)


main()
