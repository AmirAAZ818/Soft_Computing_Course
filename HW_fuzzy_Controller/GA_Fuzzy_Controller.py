import numpy as np


class Fuzzy_Controller:

    def __init__(self, population,max_gen, k):
        self.population = population
        self.N = max_gen
        self.k = k
        self.prev_bsf = 0
        self.prev_pm = 0
    def fuzzifier(self, cur_gen, p_m, cur_bsf ):
        if cur_gen % self.k != 0:
            return

        def CM(self, cur_bsf):
            cm = self.prev_bsf / cur_bsf
            return cm

        cm = CM(cur_bsf)











    def fuzifify_generation(self,gen):
        
        """ this method gets the number of current generations
            and calculate the gen / max gen and fuzzify the result.
            it returns the result as a dictionary with three keys (start, middle, end)
            these keys are the labels of fuzzy sets """
        
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
        

    def fuzzify_cm(self, current_bst, last_best,maximize=False):

        """ the set for cm in minimize and maximize is diffrent.
            to slve this problem and use uniq sets, we use diffrent formula 
            for cm.
            minimize parameter shows that we want to maximize or not.
        """
        cm = current_bst / last_best
        if maximize:
            cm = 1 / cm
        
        if cm < 0.7:
            return {'low':1, 'high':0}
        else:
            return {'low':(3.33 * cm) - 3.33, 'high':(3.33 * cm) -2.33}


    def fuzzify_lastpm(self,lastpm):

        if lastpm < 0.001:
            return {'low':1, 'aveage':0, 'high':0}
        elif lastpm < 0.005:
            return {'low':(-250*lastpm)+1.25, 'aveage':(250*lastpm)-0.25, 'high':0}
        elif lastpm < 0.01:
            return {'low':0, 'aveage':(-200*lastpm)+2, 'high':(200*lastpm)-1}
        else:
            return {'low':0, 'aveage': 0, 'high':1}
        

# testing 
def main():
    fuzzy = Fuzzy_Controller(10,100)
    gen = 10
    x = fuzzy.fuzifify_generation(gen)
    print(f'fuzzified generation for gen {gen} and max gen {fuzzy.N} ', x)
    print('---------------')
    cbest = 10
    lbest = 20
    y = fuzzy.fuzzify_cm(cbest, lbest)
    print(f'fuzzified cm for current best {cbest} and last best {lbest} ', y)
    print('---------------')
    pm = 0.002
    z = fuzzy.fuzzify_lastpm(pm)
    print(f'fuzzified pm for pm {pm} ', z)



if __name__ == "__main__":
    main()