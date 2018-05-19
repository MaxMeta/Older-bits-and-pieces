#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 18 21:45:54 2016

@author: SpiffKringle
"""

class Booger(object):
    
    def __init__(self,name,age,):
        self.name = name
        self.age = age
        self.ls = []
    
    def AddItem(self,item):
        self.ls.append(item)
    
    def __add__(self,other):
        return self.age + other.age
        
    def __sub__(self,other):
        return self.age - other.age
        
    def __getitem__(self,index):
        return self.ls[index]

    def __setitem__(self,index,item):
        self.ls[index] = item
        
        
        
class Anna(Booger):
    def __init__(self,husband = "Jeremy"):
        Booger.__init__(self,"Anna","36")
        self.husband = husband
        
    def DeclareBooger(self):
        print("I AM A BOOGER!!!!!")
    
    def __str__(self):
        return "My name is %s and I am %s years old. I am a massive booger"\
        %(self.name, self.age)