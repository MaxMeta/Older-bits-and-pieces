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
    
    
def RunSim(NumTrials,red_base_rate, green_base_rate,initial_size=1,mu=1,sigma = 1):
    
    for i in range(NumTrials):
        red_bowl = Bowl(red_base_rate,"red",intial_size,mu,sigma)
        green_bowl = Bowl(green_base_rate,"green", intial_size,mu,sigma)
        
    
        
    