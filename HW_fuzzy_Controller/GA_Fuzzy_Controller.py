import numpy as np


class Fuzzy_Controller:

    def __init__(self, population,max_gen):
        self.population = population
        self.N = max_gen
        
    def defuzifify_generation(self,gen):
        
        """ this method gets the number of current generation
            and calculata the gen / max gen and fuzify the result.
            it returns the result as a dictionary with 3 keys(start, middle, end)
            this keys are the lables of fuzy sets """
        
        x = gen / self.N
        # for range 0 to 0.4 : start is 1 else is 0
        if x < 0.4 :
            return {'start':1, 'middle':0, 'end':0}
        
        # for range 0.4 to 0.6 : start is -5x+3, middle is 5x-2, end is 0
        elif x < 0.6:
            return {'start':(-5*x)+3, 'middle':(5*x)-2, 'end':0}
        
        # for range 0.6 to 0.8 : start is 0, middle is -5x+4, end is 5x-3
        elif x < 0.8:
            return {'start':0, 'middle':(-5*x)+4, 'end':(5*x)-3}
        
        # for range 0.8 to 1 : end is 1 else is 0
        else:
            return {'start':0, 'middle':0, 'end':1}