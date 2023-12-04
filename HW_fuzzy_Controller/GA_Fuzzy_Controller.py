import numpy as np
import Membership_functions as mfs


class Fuzzy_Controller:

    def __init__(self, population, max_gen, k):
        self.population = population
        self.N = max_gen
        self.k = k
        self.prev_bsf = 0
        self.prev_pm = 0

        self.mf_pm = {"low": mfs.trapmf_maker([0, 1], 0, [0, 1e-3], 5e-3),
                      "avg": mfs.trimf_maker([0, 1], 1e-3, 5e-3, 1e-2),
                      "high": mfs.trapmf_maker([0, 1], 5e-3, [1e-2, 15e-3], 15e-3)}

        self.mf_cm = {"low": mfs.trapmf_maker([0, float("inf")], 0, [0, 7e-1], 99e-2),
                      "high": mfs.trapmf_maker([0, float("inf")], 7e-1, [1, float("inf")], float("inf"))}

        self.mf_gen = {"start": mfs.trapmf_maker([0, 1], 0, [0, 4e-1], 6e-1),
                       "middle": mfs.trimf_maker([0, 1], 0.4, 0.6, 0.8),
                       "end": mfs.trapmf_maker([0, 1], 6e-1, [8e-1, 1], 1)}

    def fuzzifier(self, cur_gen, p_m, cur_bsf):
        membership_values = {"cm": None, "pm_prev": None, "gen": None}
        if cur_gen % self.k != 0:
            return

        def CM(cur_bsf):
            """
            if cm gets closer to one, it means that algorithm is not making the desired amount of progress
            :param cur_bsf: a number, the best so far of the current generation
            :return:  0< cm <inf
            """
            cm = self.prev_bsf / cur_bsf + 1e-3
            return cm

        cm = CM(cur_bsf)

        membership_values["pm_prev"] = self.fuzzify_pm(p_m)
        membership_values['cm'] = self.fuzzify_cm(cm)
        membership_values['gen'] = self.fuzifify_generation(cur_gen)

    def fuzifify_generation(self, gen):
        """ this method gets the number of current generations
            and calculate the gen / max gen and fuzzify the result.
            it returns the result as a dictionary with three keys (start, middle, end)
            these keys are the labels of fuzzy sets """

        x = gen / self.mf_gen
        start_mf = self.mf_gen["start"]
        middle_mf = self.mf_gen["middle"]
        end_mf = self.mf_gen["end"]

        return {"start": start_mf(x), "middle": middle_mf(x), "end": end_mf(x)}

    def fuzzify_cm(self, cm):
        """ the set for cm in minimize and maximize is diffrent.
            to slve this problem and use uniq sets, we use diffrent formula 
            for cm.
            minimize parameter shows that we want to maximize or not.
        """
        low_mf = self.mf_cm["low"]
        high_mf = self.mf_cm["high"]

        return {"low": low_mf(cm), "high": high_mf(cm)}

    def fuzzify_pm(self, p_m):
        low_mf = self.mf_pm["low"]
        avg_mf = self.mf_pm["avg"]
        high_mf = self.mf_pm["high"]

        return {"low": low_mf(p_m), "avg": avg_mf(p_m), "high": high_mf(p_m)}


# testing 
def main():
    fuzzy = Fuzzy_Controller(10, 100)
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

