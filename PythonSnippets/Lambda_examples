#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 22 13:54:15 2016

@author: SpiffKringle
"""

def MakeIncrementor(n): return lambda x: x + n
import random
inc2 = MakeIncrementor(2)
inc3 = MakeIncrementor(3)

inc2(1)

inc2(3)

inc3(1)

inc3(3)


def NoiseMaker(magnitude): return lambda x: x + random.random()*magnitude * random.choice([+1,-1])

N1 = NoiseMaker(1)
N10 = NoiseMaker(10)
N100 = NoiseMaker(100)

print("N1")
for i in range(10):
    print(N1(1))

print("N10")
for i in range(10):
    print(N10(1))
    
print("N100")
for i in range(10):
    print(N100(1))
    
foo = [2, 18, 9, 22, 17, 24, 8, 12, 27]

#here is a nifty trick

def multiply(x):
    return (x*x)
def add(x):
    return (x+x)

funcs = [multiply, add]
for i in range(5):
    value = list(map(lambda x: x(i), funcs))
    print(value)
    
#Note thar map applys the specified fucntion to an iterable
#in this case, the function is something which calls whatever is passed to it
#x is taken from funcs and called on the incrementor i
#If you want to call a bunch of functions on a bunch of inputs this is a
#good way to do it
#See the "traditional" usage below for clarificatino of why this is cool


#Check this shit out!

vals = [1,2,3]

NewVals = list(map(lambda x: "the output of %s" %x, vals))


functions = {"one":lambda x: x+1, "two": lambda x: x +2, "three": lambda x: x+3}

inputs = [1,2,3]

Processed = {function:[functions[function](i) for i in inputs] for function in functions}
             
z = zip(["one","two","three"],[1,2,3])




