#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 15 14:39:49 2017

@author: owenje
"""

import random

class Bowl(object):
    
    def __init__(self,base_rate,label,initial_size=1,mu=1,sigma = 1):
        self.initial_size= initial_size
        self.variable_rate = random.gauss(mu,sigma)
        self.base_rate = base_rate
        self.label = label
        self.final_size = initial_size + initial_size*(self.variable_rate + base_rate)
        
    def GetSize(self):
        return self.final_size
        
    def GetLabel(self):
        return self.label
        
    def __str__(self):
        return "this is a %s bowl with size %s"%(self.label,self.final_size)
        
    def __lt__(self,other):
        return self.final_size < other.final_size
        
    def __gt__(self,other):
        return self.final_size > other.final_size
        
    def __eq__(self,other):
        return self.final_size  == other.final_size    
        
def RunSim(NumTrials,red_base_rate, green_base_rate,initial_size=1,mu=1,sigma = 1):
   
    max_items = []
    min_items = []
    
    for i in range(NumTrials):
        red_bowl = Bowl(red_base_rate,"red",initial_size,mu,sigma)
        green_bowl = Bowl(green_base_rate,"green", initial_size, mu,sigma)
        #print(red_bowl,green_bowl, red_bowl > green_bowl, red_bowl < green_bowl)
        max_items.append(max(red_bowl,green_bowl))
        min_items.append(min(red_bowl,green_bowl))
        
    max_of_mins = max(min_items)
    events = 0
    
    while max_items:
        if max_items.pop() < max_of_mins:
            events += 1
    return events
    
def RunSim2(NumTrials=10,red_base_rate=1, green_base_rate=1,initial_size=1,red_mu=1,red_sigma = 1,green_mu=1,green_sigma = 1):
    
    max_items = []
    min_items = []
    
    for i in range(NumTrials):
        red_bowl = Bowl(red_base_rate,("red", i),initial_size,red_mu,red_sigma)
        green_bowl = Bowl(green_base_rate,("green", i), initial_size, green_mu,green_sigma)
        #print(red_bowl,green_bowl, red_bowl > green_bowl, red_bowl < green_bowl)
        max_items.append(max(red_bowl,green_bowl))
        min_items.append(min(red_bowl,green_bowl))
        
    greater_than = 0
    less_than = 0
    
    while max_items:
        item = max_items.pop()
        for i in min_items:
            if not i.label[1] == item.label[1]:
                if i > item:
                    greater_than +=1
                else:
                    less_than += 1
                    
    return greater_than/(greater_than + less_than)
    
def RunRandomSim(NumTrials=1000,red_base_rate=1, green_base_rate=2,initial_size=1,red_mu=1,red_sigma = 1,green_mu=1,green_sigma = 1):
    #thinking that there is a bug in this right now...
    max_items = []
    min_items = []
    
    for i in range(NumTrials):
        first_tuple = random.choice([(red_base_rate, "red"), (green_base_rate,"green")])
        second_tuple = random.choice([(red_base_rate, "red"), (green_base_rate,"green")])
        first_base_rate = first_tuple[0]
        first_colour = first_tuple[1]
        second_base_rate = second_tuple[0]
        second_colour = second_tuple[1]
        first_bowl = Bowl(first_base_rate,(first_colour, i),initial_size,red_mu,red_sigma)
        second_bowl = Bowl(second_base_rate,(second_colour, i), initial_size, green_mu,green_sigma)
        print(first_bowl)
        print(second_bowl)
        print("***")
        max_items.append(max(first_bowl,second_bowl))
        min_items.append(min(first_bowl,second_bowl))
        
    greater_than = 0
    less_than = 0
    
    while max_items:
        item = max_items.pop()
        for i in min_items:
            if not i.label[1] == item.label[1]:
                if i > item:
                    greater_than +=1
                else:
                    less_than += 1
                    
    return greater_than/(greater_than + less_than)

def RunRandomSim2(NumTrials=10,red_base_rate=1, green_base_rate=1,initial_size=1,red_mu=1,red_sigma = 1,green_mu=1,green_sigma = 1):
    
    max_items = []
    min_items = []
    
    for i in range(NumTrials):
        first_tuple = random.choice([(red_base_rate, "red"), (green_base_rate,"green")])
        second_tuple = random.choice([(red_base_rate, "red"), (green_base_rate,"green")])
        first_base_rate = first_tuple[0]
        first_colour = first_tuple[1]
        second_base_rate = second_tuple[0]
        second_colour = second_tuple[1]
        first_bowl = Bowl(first_base_rate,(first_colour, i),initial_size,red_mu,red_sigma)
        second_bowl = Bowl(second_base_rate,(second_colour, i), initial_size, green_mu,green_sigma)
        #print(red_bowl,green_bowl, red_bowl > green_bowl, red_bowl < green_bowl)
        if max(first_bowl.final_size,second_bowl.final_size)/min((first_bowl.final_size,second_bowl.final_size)) > 2*red_sigma:
            max_items.append(max(first_bowl,second_bowl))
            min_items.append(min(first_bowl,second_bowl))
        
    max_of_mins = max(min_items)
    events = 0
    
    while max_items:
        if max_items.pop() < max_of_mins:
            events += 1
    return events

def RunMany(NumSims = 10000,NumTrials=10,red_base_rate=1, green_base_rate=1, initial_size=1,
            red_mu=5,red_sigma = 1,green_mu=5, green_sigma = 1):
    
    Sims = []
    
    for i in range(NumSims):
        Sims.append(RunRandomSim2(NumTrials,red_base_rate, green_base_rate, initial_size,
                            red_mu,red_sigma,green_mu,green_sigma ))
        
    return sum(Sims)/len(Sims)

for i in range(10):
    red_base_rate = 1 + i    
    z = RunMany(red_base_rate=red_base_rate)
    print(z)    

"""
Red_base_rate 1 - 10, both sigmas = 1.0, mu = 1.0

0.16663111111111262
0.1263444444444453
0.05576111111111234
0.014421111111111235
0.002146666666666699
0.0002077777777777774
1.2222222222222222e-05
1.1111111111111112e-06
0.0
0.0


Red_base_rate 1 - 10, both sigmas = 0.8, mu = 1.0

0.16691777777777994
0.10833555555555617
0.029678888888889435
0.0036533333333334567
0.00019555555555555518
3.3333333333333333e-06
0.0
0.0
0.0
0.0


Red_base_rate 1 - 10, both sigmas = 0.6, mu = 1.0

0.16604333333333557
0.07865111111111185
0.008147777777777962
0.00021222222222222188
2.2222222222222225e-06
0.0
0.0
0.0
0.0
0.0


Red_base_rate 1 - 10, both sigmas = 0.4, mu = 1.0

0.16657000000000188
0.0305344444444452
0.0001899999999999997
0.0
0.0
0.0
0.0
0.0
0.0
0.0


Red_base_rate 1 - 10, both sigmas = 0.2, mu = 1.0

0.16579777777777968
0.00018333333333333298
0.0
0.0
0.0
0.0
0.0
0.0
0.0
0.0


Red_base_rate 1 - 10, both sigmas = 0.1, mu = 1.0

0.16762444444444646
0.0
0.0
0.0
0.0
0.0
0.0
0.0
0.0
0.0

"""

#think of the case in which the only source of variation is the variation in base rate, 
#if this differs at all, they segregate by red and green and no pair max is ever smaller than any pair min
# as sigma increases, this effect gets hidden but is revealed on repeated trials
#The ratio of sigma/base_rate_difference determines how large the effect is