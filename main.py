from random import randint, random


class BGA:
    def __init__(self, optimization_function, parameters_number, Choromosom_bits, population, 
                 crossover_rate, mutation_rate):
        self.Function = optimization_function # تابع هدف
        self.Parameters = parameters_number # تعداد پارامترهای تابع 
        self.Population = population # اندازه جمعیت
        self.Choromosom_Len = Choromosom_bits
        self.Pc = crossover_rate
        self.pm = mutation_rate
        