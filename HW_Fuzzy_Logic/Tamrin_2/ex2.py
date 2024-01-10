from functions import *
import numpy as np

class Fuzzy_food_control:
    def __init__(self, temp, vol, tc):
        self.t = temp
        self.v = vol
        self.c = tc
        self.resultdef = {'tooshort': trimf_maker(domain=[0,100], start=0, peak=0, end=25)
                     , 'short':trimf_maker(domain=[0,100], start=0, peak=25, end=50),
                       'medium':trimf_maker(domain=[0,100], start=25, peak=50, end=75)
                       , 'long':trimf_maker(domain=[0,100], start=50, peak=75, end=100)
                       , 'toolong':trimf_maker(domain=[0,100], start=75, peak=100, end=100)}

    def run(self):
        c = self.fuzzify()
        a = self.matching(c)
        b = self.inference(a)
        x = self.defuzzify(b)
        print(f'Requierd time : {x}')

    def fuzzify_res(self, x):
        tooshort = self.resultdef['tooshort'](x)
        short = self.resultdef['short'](x)
        medium = self.resultdef['medium'](x)
        lng = self.resultdef['long'](x)
        toolong = self.resultdef['toolong'](x)

        return {'tooshort': tooshort, 'short':short, 'medium':medium, 'long':lng, 'toolong':toolong}

    def fuzzify(self):

        def temp(t):

            flow = trimf_maker(domain=[0,100],start=0, peak=0, end=50)
            favg = trimf_maker(domain=[0,100], start=0, peak=50, end=100)
            fhigh = trimf_maker(domain=[0,100],start=50, peak=100, end=100)
            degress = {'low':flow(t), 'average':favg(t), 'high':fhigh(t)}
            return degress
        
        def volume(v):

            flittle = trimf_maker(domain=[0,1000],start=0, peak=0, end=500)
            fmedium = trimf_maker(domain=[0,1000], start=0, peak=500, end=1000)
            fbig = trimf_maker(domain=[0,1000],start=500, peak=1000, end=1000)
            degrees = {'little':flittle(v), 'medium':fmedium(v), 'big':fbig(v)}
            return degrees
        
        def transmisiin(c):

            flow = trimf_maker(domain=[0,100],start=0, peak=0, end=50)
            favg = trimf_maker(domain=[0,100], start=0, peak=50, end=100)
            fhigh = trimf_maker(domain=[0,100],start=50, peak=100, end=100)
            degress = {'low':flow(c), 'average':favg(c), 'high':fhigh(c)}
            return degress

        tempdegress = temp(t=self.t)
        voldegrees = volume(v=self.v)
        tcdegrees = transmisiin(c=self.c)
        return {'temp':tempdegress, 'volume':voldegrees, 'transmision':tcdegrees}

    def matching(self, degrees):
        membership_rules = {'tooshort':[], 'short':[], 'medium':[], 'long':[], 'toolong':[]}

        # rule1
        r1 = min(degrees['temp']['low'], degrees['volume']['little'], degrees['transmision']['low'])
        membership_rules['long'].append(r1)

        # rule2
        r2 = min(degrees['temp']['low'], degrees['volume']['little'], degrees['transmision']['average'])
        membership_rules['medium'].append(r2)

        # rule3
        r3 = min(degrees['temp']['low'], degrees['volume']['little'], degrees['transmision']['high'])
        membership_rules['short'].append(r3)

        # rule4
        r4 = min(degrees['temp']['low'], degrees['volume']['medium'], degrees['transmision']['low'])
        membership_rules['medium'].append(r4)

        # rule5
        r5 = min(degrees['temp']['low'], degrees['volume']['medium'], degrees['transmision']['average'])
        membership_rules['medium'].append(r5)

        # rule6
        r6 = min(degrees['temp']['low'], degrees['volume']['medium'], degrees['transmision']['high'])
        membership_rules['long'].append(r6)

        # rule7
        r7 = min(degrees['temp']['low'], degrees['volume']['big'], degrees['transmision']['low'])
        membership_rules['toolong'].append(r7)

        # rule8
        r8 = min(degrees['temp']['low'], degrees['volume']['big'], degrees['transmision']['average'])
        membership_rules['long'].append(r8)

        # rule9
        r9 = min(degrees['temp']['low'], degrees['volume']['big'], degrees['transmision']['high'])
        membership_rules['long'].append(r9)

        # rule10
        r10 = min(degrees['temp']['average'], degrees['volume']['little'], degrees['transmision']['low'])
        membership_rules['short'].append(r10)

        # rule11
        r11 = min(degrees['temp']['average'], degrees['volume']['little'], degrees['transmision']['average'])
        membership_rules['short'].append(r11)

        # rule12
        r12 = min(degrees['temp']['average'], degrees['volume']['little'], degrees['transmision']['high'])
        membership_rules['short'].append(r12)

        # rule13
        r13 = min(degrees['temp']['average'], degrees['volume']['medium'], degrees['transmision']['low'])
        membership_rules['medium'].append(r13)

        # rule14
        r14 = min(degrees['temp']['average'], degrees['volume']['medium'], degrees['transmision']['average'])
        membership_rules['medium'].append(r14)

        # rule15
        r15 = min(degrees['temp']['average'], degrees['volume']['medium'], degrees['transmision']['high'])
        membership_rules['short'].append(r15)

        # rule16
        r16 = min(degrees['temp']['average'], degrees['volume']['big'], degrees['transmision']['low'])
        membership_rules['long'].append(r16)

        # rule17
        r17 = min(degrees['temp']['average'], degrees['volume']['big'], degrees['transmision']['average'])
        membership_rules['medium'].append(r17)

        # rule18
        r18 = min(degrees['temp']['average'], degrees['volume']['big'], degrees['transmision']['high'])
        membership_rules['medium'].append(r18)

        # rule19
        r19 = min(degrees['temp']['high'], degrees['volume']['little'], degrees['transmision']['low'])
        membership_rules['short'].append(r19)

        # rule20
        r20 = min(degrees['temp']['high'], degrees['volume']['little'], degrees['transmision']['average'])
        membership_rules['medium'].append(r20)

        # rule21
        r21 = min(degrees['temp']['high'], degrees['volume']['little'], degrees['transmision']['high'])
        membership_rules['short'].append(r21)

        # rule22
        r22 = min(degrees['temp']['high'], degrees['volume']['medium'], degrees['transmision']['low'])
        membership_rules['long'].append(r22)

        # rule23
        r23 = min(degrees['temp']['high'], degrees['volume']['medium'], degrees['transmision']['average'])
        membership_rules['medium'].append(r23)

        # rule24
        r24 = min(degrees['temp']['high'], degrees['volume']['medium'], degrees['transmision']['high'])
        membership_rules['short'].append(r24)

        # rule25
        r25 = min(degrees['temp']['high'], degrees['volume']['big'], degrees['transmision']['low'])
        membership_rules['toolong'].append(r25)

        # rule26
        r26 = min(degrees['temp']['high'], degrees['volume']['big'], degrees['transmision']['average'])
        membership_rules['long'].append(r26)

        # rule27
        r27 = min(degrees['temp']['high'], degrees['volume']['big'], degrees['transmision']['high'])
        membership_rules['medium'].append(r27)

        return membership_rules
    
    def inference(self, membership_rules:dict):
        fuzzy_sets = list(membership_rules.keys())
        fuzzy_output ={}
        for f_set in fuzzy_sets:
            if membership_rules[f_set] != []:
                fuzzy_output[f_set] = max(membership_rules[f_set])
            else:
                fuzzy_output[f_set] = 0

        return fuzzy_output

    def defuzzify(self, fuzzy_output):
        
        def COG(X, f_output):
            membership_degrees = []
            for x in X:
                f_var = self.fuzzify_res(x)
                md = max(min(f_output['tooshort'], f_var['tooshort']), min(f_output['short'], f_var['short']),
                         min(f_output['medium'], f_var['medium']),min(f_output['long'], f_var['long']),
                         min(f_output['toolong'], f_var['toolong']))
                membership_degrees.append(md)
            membership_degrees = np.array(membership_degrees)

            cog = np.dot(membership_degrees, X) / np.sum(membership_degrees)
            return cog

        X = np.arange(0,100,0.001) 
        return COG(X, fuzzy_output)
    
