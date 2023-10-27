from random import randint, random


# class for BGA Algo

class BGA:
    def __init__(self, optimization_function, parameters_number,choromosom_bits, population, 
                 crossover_rate, mutation_rate):
        self.Function = optimization_function # تابع هدف
        self.Parameters = parameters_number # تعداد پارامترهای تابع 
        self.Population = population # اندازه جمعیت
        self.Choromosom_Len = choromosom_bits
        self.Pc = crossover_rate
        self.pm = mutation_rate


    def Random_Choromosom(self):
        population_matrix = []
        for i in range(self.Population):
            choro = []
            for j in range(self.Choromosom_Len):
                choro[j] = randint(0,1)
            population_matrix[i] = choro
        return population_matrix
    

    def Mutation(self, child_matrix):
        rand = random()
        if rand > self.pm :
            return
        else:
            i = randint(0,self.Population-1)
            j = randint(0,self.Choromosom_Len-1)
            child_matrix[i,j] = not child_matrix[i,j]
            return
