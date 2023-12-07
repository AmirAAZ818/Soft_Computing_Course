import numpy as np
import Membership_functions as mfs
import matplotlib.pyplot as plt

class Fuzzy_Controller:

    def __init__(self, max_gen, k):
        """

        :param max_gen: Maximum number of generations.
        :param k: The interval of each control action.
        :param defuzzifier_method: The method
        which will be used in defuzzification phase
        when evaluating the crisp value from the fuzzy output.
        """
        self.N = max_gen
        self.k = k
        self.prev_bsf = 0
        self.prev_pm = 0
        self.pm_history = []

        self.mf_pm = {"low": mfs.trapmf_maker([0, 1], 0, [0, 1e-3], 5e-3),
                      "avg": mfs.trimf_maker([0, 1], 1e-3, 5e-3, 1e-2),
                      "high": mfs.trapmf_maker([0, 1], 5e-3, [1e-2, 1], 1)}

        self.mf_cm = {"low": mfs.trapmf_maker([0, float("inf")], 0, [0, 7e-1], 99e-2),
                      "high": mfs.trapmf_maker([0, float("inf")], 7e-1, [1, float("inf")], float("inf"))}

        self.mf_gen = {"start": mfs.trapmf_maker([0, 1], 0, [0, 4e-1], 6e-1),
                       "middle": mfs.trimf_maker([0, 1], 0.4, 0.6, 0.8),
                       "end": mfs.trapmf_maker([0, 1], 6e-1, [8e-1, 1], 1)}

    def control(self, cur_gen, p_m, cur_bsf):
        """
        This method is runs the whole system.
        :param cur_gen: A number, the current iteration of the algorithm
        :param p_m: A number, current mutation rate
        :param cur_bsf: A number, the current best so far of the algorithm
        :return: a crisp number for mutation rate
        """
        self.pm_history.append(p_m)

        if cur_gen % self.k != 0:
            return p_m

        # Logging pm

        # Fuzzifying phase
        fuzzy_vars = self.fuzzifier(cur_gen=cur_gen, p_m=p_m, cur_bsf=cur_bsf)

        # Updating bsf and pm for the next control phase
        self.prev_bsf = cur_bsf
        self.prev_pm = p_m
        # print(f"________cur gen is : {cur_gen}________")
        # print(fuzzy_vars)

        pm_strengths = self.matching(fuzzy_vars=fuzzy_vars)
        pm_fuzzy_output = self.inference(pm_strengths)
        crisp_pm = self.defuzzifier(pm_fuzzy_output)

        return crisp_pm

    def defuzzifier(self, fuzzy_output):
        """
        This method is defuzzify the fuzzy output with COG method
        :param fuzzy_output: A dict which represents a fuzzy output with items "fuzzy set: membership degree"
        :return: A crisp value that is the output of the controller
        """

        def COG(X, f_output):
            membership_degrees = []
            for x in X:
                f_var = self.fuzzify_pm(x)
                md = max(min(f_output['low'], f_var['low']), min(f_output['avg'], f_var['avg']), min(f_output['high'], f_var['high']))
                membership_degrees.append(md)

            membership_degrees = np.array(membership_degrees)
            cog = np.dot(membership_degrees, X) / np.sum(membership_degrees)

            return cog


        X = np.arange(0, 1.0001, 1e-4)
        return COG(X, fuzzy_output)



    def inference(self, pm_fuzzy):
        """
        This method is for the inference and combination phase of the algorithm
        :param pm_fuzzy: A dict where keys represent the sets defined for the variable the fuzzy output from the matching phase.
        :return: A dict where its keys are the same as pm_fuzzy keys,
        this dict represents a fuzzy variable with its fuzzy sets defined on it,
        representing the fuzzy output of the inference engine.
        """
        fuzzy_sets = list(pm_fuzzy.keys())
        fuzzy_output = {f_set: max(pm_fuzzy[f_set]) for f_set in fuzzy_sets}
        # print(f"fuzzy output is : {fuzzy_output}")
        return fuzzy_output

    def matching(self, fuzzy_vars):
        """
        This method implements the matching phase of the control,
        where we evaluate the strength the outcome of each rule.
        :param fuzzy_vars: A dict containing 3 other dicts which are fuzzified inputs
        :return: a dict,
        which is the pm strengths for each set defined on the variable
        """
        pm_strengths = {"low": [], "avg": [], "high": []}

        # Rule 1
        r1s = min(fuzzy_vars['cm']['high'], fuzzy_vars['pm_prev']['low'], fuzzy_vars['gen']['start'])
        pm_strengths['avg'].append(r1s)

        # Rule 2
        r2s = min(fuzzy_vars['cm']['high'], fuzzy_vars['pm_prev']['avg'], fuzzy_vars['gen']['start'])
        pm_strengths['high'].append(r2s)

        # Rule 3
        r3s = min(fuzzy_vars['cm']['high'], fuzzy_vars['pm_prev']['high'], fuzzy_vars['gen']['start'])
        pm_strengths['low'].append(r3s)

        # Rule 4
        r4s = min(fuzzy_vars['cm']['low'], fuzzy_vars['pm_prev']['low'], fuzzy_vars['gen']['start'])
        pm_strengths['low'].append(r4s)

        # Rule 5
        r5s = min(fuzzy_vars['cm']['low'], fuzzy_vars['pm_prev']['avg'], fuzzy_vars['gen']['start'])
        pm_strengths['low'].append(r5s)

        # Rule 6
        r6s = min(fuzzy_vars['cm']['low'], fuzzy_vars['pm_prev']['high'], fuzzy_vars['gen']['start'])
        pm_strengths['avg'].append(r6s)

        # Rule 7
        r7s = min(fuzzy_vars['cm']['high'], fuzzy_vars['pm_prev']['low'], fuzzy_vars['gen']['middle'])
        pm_strengths['avg'].append(r7s)

        # Rule 8
        r8s = min(fuzzy_vars['cm']['high'], fuzzy_vars['pm_prev']['avg'], fuzzy_vars['gen']['middle'])
        pm_strengths['avg'].append(r8s)

        # Rule 9
        r9s = min(fuzzy_vars['cm']['high'], fuzzy_vars['pm_prev']['high'], fuzzy_vars['gen']['middle'])
        pm_strengths['low'].append(r9s)

        # Rule 10
        r10s = min(fuzzy_vars['cm']['low'], fuzzy_vars['pm_prev']['low'], fuzzy_vars['gen']['middle'])
        pm_strengths['avg'].append(r10s)

        # Rule 11
        r11s = min(fuzzy_vars['cm']['low'], fuzzy_vars['pm_prev']['avg'], fuzzy_vars['gen']['middle'])
        pm_strengths['avg'].append(r11s)

        # Rule 12
        r12s = min(fuzzy_vars['cm']['low'], fuzzy_vars['pm_prev']['high'], fuzzy_vars['gen']['middle'])
        pm_strengths['high'].append(r12s)

        # Rule 13
        r13s = min(fuzzy_vars['cm']['high'], fuzzy_vars['pm_prev']['low'], fuzzy_vars['gen']['end'])
        pm_strengths['avg'].append(r13s)

        # Rule 14
        r14s = min(fuzzy_vars['cm']['high'], fuzzy_vars['pm_prev']['avg'], fuzzy_vars['gen']['end'])
        pm_strengths['high'].append(r14s)

        # Rule 15
        r15s = min(fuzzy_vars['cm']['high'], fuzzy_vars['pm_prev']['high'], fuzzy_vars['gen']['end'])
        pm_strengths['low'].append(r15s)

        # Rule 16
        r16s = min(fuzzy_vars['cm']['low'], fuzzy_vars['pm_prev']['low'], fuzzy_vars['gen']['end'])
        pm_strengths['avg'].append(r16s)

        # Rule 17
        r17s = min(fuzzy_vars['cm']['low'], fuzzy_vars['pm_prev']['avg'], fuzzy_vars['gen']['end'])
        pm_strengths['high'].append(r17s)

        # Rule 18
        r18s = min(fuzzy_vars['cm']['low'], fuzzy_vars['pm_prev']['high'], fuzzy_vars['gen']['end'])
        pm_strengths['avg'].append(r18s)

        return pm_strengths

    def fuzzifier(self, cur_gen, p_m, cur_bsf):
        """
        This method does the fuzzifing phase of the FCS.
        :param cur_gen: the current iteration of the genetic algorithm.
        :param p_m: the current mutation rate of the genetic algorithm.
        :param cur_bsf: the best so far up do this generation of the algorithm.
        :return: fizzified input params as a dict.
        """
        membership_values = {"cm": None, "pm_prev": None, "gen": None}

        def CM(cur_bsf):
            """
            if cm gets closer to one, it means that algorithm is not making the desired amount of progress
            :param cur_bsf: a number, the best so far of the current generation
            :return:  0< cm <inf
            """
            cm = self.prev_bsf / (cur_bsf + 1e-3)
            return cm

        cm = CM(cur_bsf)

        membership_values["pm_prev"] = self.fuzzify_pm(p_m)
        membership_values['cm'] = self.fuzzify_cm(cm)
        membership_values['gen'] = self.fuzzifify_generation(cur_gen)

        return membership_values

    def fuzzifify_generation(self, gen):
        """ this method gets the number of current generations
            and calculate the gen / max gen and fuzzify the result.
            it returns the result as a dictionary with three keys (start, middle, end)
            these keys are the labels of fuzzy sets """

        x = gen / self.N
        start_mf = self.mf_gen["start"]
        middle_mf = self.mf_gen["middle"]
        end_mf = self.mf_gen["end"]

        return {"start": start_mf(x), "middle": middle_mf(x), "end": end_mf(x)}

    def fuzzify_cm(self, cm):

        low_mf = self.mf_cm["low"]
        high_mf = self.mf_cm["high"]

        return {"low": low_mf(cm), "high": high_mf(cm)}

    def fuzzify_pm(self, p_m):
        low_mf = self.mf_pm["low"]
        avg_mf = self.mf_pm["avg"]
        high_mf = self.mf_pm["high"]

        return {"low": low_mf(p_m), "avg": avg_mf(p_m), "high": high_mf(p_m)}

    def Reset(self):
        """
        This method resets the pm and bsf of the controller,
        giving it the quality to be used multiple times for the multiple runs of the algorithm
        :return: Noting
        """
        self.prev_pm = 0
        self.prev_bsf = 0

    def plot_pm(self):
        plt.plot(np.arange(0, self.N, 1), self.pm_history)
        plt.show()


# testing
# def main():
#     fcs = Fuzzy_Controller(101, 5)
#     bsf_x = np.arange(1, 204, 2)
#     bsf = np.square(bsf_x - 15)
#
#     # plt.plot(bsf_x, bsf)
#     # plt.show()
#     print(bsf)
#     # pm = np.arange(1e-3, 0.01009, 9e-5)
#     pm = 8e-3
#     print(pm)
#     # print(len(pm))
#     print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
#     for i in range(101):
#         print(fcs.control(cur_gen=i, p_m=pm, cur_bsf=bsf[i]))
#
#
# if __name__ == "__main__":
#     main()
