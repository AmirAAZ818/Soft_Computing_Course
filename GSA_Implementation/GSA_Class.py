import matplotlib.pyplot as plt
import random
import math
from tabulate import tabulate


class GSA:

    def __init__(self, function, domain, function_dim, pop_size, ittration, k, G, a, runs, minimize=True):
        self.function = function
        self.runs = runs
        self.bound = domain
        self.dim = function_dim
        self.population_size = pop_size
        self.itters = ittration
        self.minimize = minimize
        self.t = None
        self.G0 = G
        self.G = G
        self.a = a
        self.mess = [1 for _ in range(self.population_size)]
        self.accelerate = [[0 for _ in range(self.dim)] for _ in range(self.population_size)]
        self.velacity = [[0 for _ in range(self.dim)] for _ in range(self.population_size)]
        self.forces = [[0 for _ in range(self.dim)] for _ in range(
            self.population_size)]  # matrix of forces, value of [i][j] means force of the agent i in the j diminution
        self.K = k
        self.posations = self.initial_posations()  # matrix of position
        self.fits = [0 for _ in range(self.population_size)]
        self.best = 0
        self.worst = 0
        self.bests = []
        self.avg_fits = []
        self.best_of_runs = []
        self.avg_fits_of_runs = []
        self.best_position = None
        self.best_positions = []
        self.total_best = [self.bound[0]['high'], self.best_position]

    # this method creates a random matrix (size population size x dim) and return the matrix
    def initial_posations(self):
        agents = []
        for _ in range(self.population_size):
            agent = []
            for j in range(self.dim):
                l_bound = self.bound[j]['low']
                u_bound = self.bound[j]['high']
                agent.append(random.uniform(l_bound, u_bound))
            agents.append(agent)
        return agents

    def run(self):
        self.print_parameters()
        for _ in range(self.runs):
            self.reset()
            self.one_run()
            self.log_algo()

        print(f'Best Value : {self.total_best[0]}')
        print(f'Best Position : {self.total_best[1]}')
        self.plot()

    # this method, calls methods for each step of the algorithm for itters time.
    def one_run(self):
        for i in range(self.itters):
            self.t = i
            self.get_fitness()
            self.update()
            self.calculate_force()
            self.calculate_accelerate()
            self.calculate_velacity()
            self.calculate_position()
            self.update_mess()
            self.log_one_run()

    def get_fitness(self):
        for i in range(self.population_size):
            x = self.function(self.posations[i])
            self.fits[i] = x

    # calculates the distance of two messes. inputs: mess1 & mess2 - output: distance(a float number)
    def distance(self, m1, m2):
        r = 0
        for i in range(self.dim):
            r += ((self.posations[m1][i] - self.posations[m2][i]) ** 2)
        return r ** 0.5

    # this function is the implementation of force formula
    def calculate_force(self):
        fits = self.fits.copy()
        kbests = []
        for i in range(self.K):
            if self.minimize:
                m = min(fits)
                fits.remove(m)
                indx = self.fits.index(m)
                kbests.append(indx)
            else:
                m = max(fits)
                fits.remove(m)
                indx = self.fits.index(m)
                kbests.append(indx)

        for i in range(self.population_size):
            for j in range(self.dim):
                f = 0
                totalforce = 0
                for k in kbests:
                    if k == i:
                        totalforce = 0
                    else:
                        r = self.distance(i, k)
                        f = (self.G * ((self.mess[i] * self.mess[k]) / (r + 0.001)) *
                             (self.posations[k][j] - self.posations[i][j]))
                        totalforce = totalforce + random.random() * f
                self.forces[i][j] = totalforce

    def calculate_accelerate(self):
        for i in range(self.population_size):
            if self.mess[i] == 0:
                continue
            for j in range(self.dim):
                self.accelerate[i][j] = self.forces[i][j] / self.mess[i]

    def calculate_velacity(self):
        for i in range(self.population_size):
            for j in range(self.dim):
                self.velacity[i][j] = random.random() * self.velacity[i][j] + self.accelerate[i][j]

    def calculate_position(self):
        for i in range(self.population_size):
            for j in range(self.dim):
                # self.posations[i][j] += self.velacity[i][j]
                # if self.posations[i][j] < self.bound[j]['low'] :
                #     self.posations[i][j] = self.bound[j]['low']
                # if self.posations[i][j] > self.bound[j]['high']:
                #     self.posations[i][j] = self.bound[j]['high']
                x = self.posations[i][j] + self.velacity[i][j]
                self.posations[i][j] = x if (self.bound[j]['high'] > x > self.bound[j]['low']) else \
                    self.posations[i][j]

    def update_mess(self):
        q = [0 for _ in range(self.population_size)]
        for i in range(self.population_size):
            q[i] = (self.fits[i] - self.worst) / (self.best - self.worst)
        s = sum(q)
        for i in range(self.population_size):
            self.mess[i] = q[i] / s

    def update(self):
        self.G = self.G0 * (math.exp(-self.a * (self.t / self.itters)))

        if self.minimize:
            self.worst = max(self.fits)
            self.best = min(self.fits)
        else:
            self.best = max(self.fits)
            self.worst = min(self.fits)
        indx = self.fits.index(self.best)
        self.best_position = self.posations[indx]
        if self.minimize:
            if self.total_best[0] > self.best:
                self.total_best[0] = self.best
                self.total_best[1] = self.best_position
        else:
            if self.total_best[0] < self.best:
                self.total_best[0] = self.best
                self.total_best[1] = self.best_position

    def log_one_run(self):
        self.bests.append(self.best)
        self.avg_fits.append(sum(self.fits) / self.population_size)

    def log_algo(self):
        self.best_of_runs.append(self.bests)
        self.avg_fits_of_runs.append(self.avg_fits)
        self.best_positions.append(self.best_position)

    def reset(self):
        self.posations = self.initial_posations()
        self.t = None
        self.best_position = None
        # self.fits.clear()
        self.fits = [0 for _ in range(self.population_size)]
        self.avg_fits = []
        self.bests = []
        self.best = 1
        self.worst = 0
        self.mess = [1 for _ in range(self.population_size)]
        self.accelerate = [[0 for _ in range(self.dim)] for _ in range(self.population_size)]
        self.velacity = [[0 for _ in range(self.dim)] for _ in range(self.population_size)]
        self.forces = [[0 for _ in range(self.dim)] for _ in range(self.population_size)]

    def print_parameters(self):
        # This is a method that prints parameters in tabular structure
        parameters = [
            ["Algorithm Runs", self.runs],
            ["Number Of Iterations", self.itters],
            ["Population Size", self.population_size],
            ["G0", self.G0],
            ["Effect Of Itratin In G", self.a],
            ["Function Input Shape", self.dim]
        ]
        print(tabulate(parameters, headers=["Parameter", "Value"], tablefmt="fancy_grid"))

    def plot(self):

        def get_avg(mat, n, m):
            res = []
            for i in range(m):
                s = 0
                for j in range(n):
                    s += mat[j][i]
                res.append(s / n)
            return res

        plt.style.use('Solarize_Light2')

        y2 = get_avg(self.avg_fits_of_runs, self.runs, self.itters)
        y1 = get_avg(self.best_of_runs, self.runs, self.itters)
        x = list(range(self.itters))

        plt.plot(x, y1, label="Average Fits Of Runs", color="blue")
        plt.plot(x, y2, label="Best Fit of Runs", color="red", ls="--")

        plt.legend()
        plt.show()
