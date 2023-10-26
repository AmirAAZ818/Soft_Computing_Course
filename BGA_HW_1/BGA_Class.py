
# class for BGA Algo

class BGA:
    def __init__(self, optimization_function, parameters_number, population, 
                 crossover_rate, mutation_rate):
        self.Function = optimization_function # تابع هدف
        self.Parameters = parameters_number # تعداد پارامترهای تابع 
        self.Population = population # اندازه جمعیت
        self.Pc = crossover_rate
        self.pm = mutation_rate
        