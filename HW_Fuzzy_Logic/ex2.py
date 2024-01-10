from warmuptime import *


class Fuzzy_food_control:
    def __init__(self, temp, vol, tc):
        self.t = temp
        self.v = vol
        self.c = tc
        self.degrees = None


    def run(self):
        self.fuzzify()
        a = self.matching()
        x = self.defuzzify(a)
        print(x)


    def fuzzify(self):

        def temp(t):
            degress = {'low':0, 'average':0, 'high':0}
            degress['low'] = (50 - t) / 50
            if t < 50:
                degress['average'] = t / 50
            else:
                degress['average'] = (100 - t) / 50
            degress['high'] = (t - 50) / 50

            return degress
        
        def volume(v):

            degrees = {'little':0, 'medium':0, 'big':0}
            degrees['little'] = (500 - v) / 500

            if v < 500:
                degrees['medium'] = v / 500
            else:
                degrees['medium'] = (1000 - v) / 500

            degrees['big'] = (v - 500) / 500

            return degrees
        
        def transmisiin(c):
            degress = {'low':0, 'average':0, 'high':0}

            degress['low'] = (50 - c) / 50

            if c < 50:
                degress['average'] = c / 50
            else:
                degress['average'] = (100 - c) / 50

            degress['high'] = (c - 50) / 50

            return degress

        tempdegress = temp(t=self.t)
        voldegrees = volume(v=self.v)
        tcdegrees = transmisiin(c=self.c)
        self.degrees = {'temp':tempdegress, 'volume':voldegrees, 'transmision':tcdegrees}

    
    def matching(self):
        membership_rules = {'tooshort':[], 'short':[], 'medium':[], 'long':[], 'toolong':[]}

        # rule1
        r1 = min(self.degrees['temp']['low'], self.degrees['volume']['little'], self.degrees['transmision']['low'])
        membership_rules['long'].append(r1)

        # rule2
        r2 = min(self.degrees['temp']['low'], self.degrees['volume']['little'], self.degrees['transmision']['average'])
        membership_rules['medium'].append(r2)

        # rule3
        r3 = min(self.degrees['temp']['low'], self.degrees['volume']['little'], self.degrees['transmision']['high'])
        membership_rules['short'].append(r3)

        # rule4
        r4 = min(self.degrees['temp']['low'], self.degrees['volume']['medium'], self.degrees['transmision']['low'])
        membership_rules['medium'].append(r4)

        # rule5
        r5 = min(self.degrees['temp']['low'], self.degrees['volume']['medium'], self.degrees['transmision']['averege'])
        membership_rules['medium'].append(r5)

        # rule6
        r6 = min(self.degrees['temp']['low'], self.degrees['volume']['medium'], self.degrees['transmision']['high'])
        membership_rules['long'].append(r6)

        # rule7
        r7 = min(self.degrees['temp']['low'], self.degrees['volume']['big'], self.degrees['transmision']['low'])
        membership_rules['toolong'].append(r7)

        # rule8
        r8 = min(self.degrees['temp']['low'], self.degrees['volume']['big'], self.degrees['transmision']['averege'])
        membership_rules['long'].append(r8)

        # rule9
        r9 = min(self.degrees['temp']['low'], self.degrees['volume']['big'], self.degrees['transmision']['high'])
        membership_rules['long'].append(r9)

        # rule10
        r10 = min(self.degrees['temp']['average'], self.degrees['volume']['little'], self.degrees['transmision']['low'])
        membership_rules['short'].append(r10)

        # rule11
        r11 = min(self.degrees['temp']['average'], self.degrees['volume']['little'], self.degrees['transmision']['average'])
        membership_rules['short'].append(r11)

        # rule12
        r12 = min(self.degrees['temp']['average'], self.degrees['volume']['little'], self.degrees['transmision']['high'])
        membership_rules['short'].append(r12)

        # rule13
        r13 = min(self.degrees['temp']['average'], self.degrees['volume']['medium'], self.degrees['transmision']['low'])
        membership_rules['medium'].append(r13)

        # rule14
        r14 = min(self.degrees['temp']['average'], self.degrees['volume']['medium'], self.degrees['transmision']['average'])
        membership_rules['medium'].append(r14)

        # rule15
        r15 = min(self.degrees['temp']['average'], self.degrees['volume']['medium'], self.degrees['transmision']['high'])
        membership_rules['short'].append(r15)

        # rule16
        r16 = min(self.degrees['temp']['average'], self.degrees['volume']['big'], self.degrees['transmision']['low'])
        membership_rules['long'].append(r16)

        # rule17
        r17 = min(self.degrees['temp']['average'], self.degrees['volume']['big'], self.degrees['transmision']['average'])
        membership_rules['medium'].append(r17)

        # rule18
        r18 = min(self.degrees['temp']['average'], self.degrees['volume']['big'], self.degrees['transmision']['high'])
        membership_rules['medium'].append(r18)

        # rule19
        r19 = min(self.degrees['temp']['high'], self.degrees['volume']['little'], self.degrees['transmision']['low'])
        membership_rules['short'].append(r19)

        # rule20
        r20 = min(self.degrees['temp']['high'], self.degrees['volume']['little'], self.degrees['transmision']['average'])
        membership_rules['medium'].append(r20)

        # rule21
        r21 = min(self.degrees['temp']['high'], self.degrees['volume']['little'], self.degrees['transmision']['high'])
        membership_rules['short'].append(r21)

        # rule22
        r22 = min(self.degrees['temp']['high'], self.degrees['volume']['medium'], self.degrees['transmision']['low'])
        membership_rules['long'].append(r22)

        # rule23
        r23 = min(self.degrees['temp']['high'], self.degrees['volume']['medium'], self.degrees['transmision']['average'])
        membership_rules['medium'].append(r23)

        # rule24
        r24 = min(self.degrees['temp']['high'], self.degrees['volume']['medium'], self.degrees['transmision']['high'])
        membership_rules['short'].append(r24)

        # rule25
        r25 = min(self.degrees['temp']['high'], self.degrees['volume']['big'], self.degrees['transmision']['low'])
        membership_rules['toolong'].append(r25)

        # rule26
        r26 = min(self.degrees['temp']['high'], self.degrees['volume']['big'], self.degrees['transmision']['average'])
        membership_rules['long'].append(r26)

        # rule27
        r27 = min(self.degrees['temp']['high'], self.degrees['volume']['big'], self.degrees['transmision']['high'])
        membership_rules['medium'].append(r27)

        return membership_rules

    def defuzzify(self, rules):
        pass
        # return x