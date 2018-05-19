#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 26 17:32:28 2017
@author: spiffkringle
"""

import math
import copy

def euler_method(Fzero,Fdash,a,increments, zero):
    if increments == 0:
        return Fzero
    print(Fzero)
    return euler_method(Fzero + Fdash(zero)*a/increments,Fdash,a-a/increments,
                        increments-1,zero + a/increments)
# y=x^2
   
euler_method(1.0,lambda x: math.e**x,1.0,100,0.0)

#2.7097047383081225

def evaluate_polynomial(f,x):
    """
    Evaluates a polynomial (given as a list) at the value x
    polynomial is a list of co efficents for example:
        [1,3,1,0,2] = 1*x^4 + 3*x^3 + 1*x^2 + 0*x^1 + 2*x^0
        note that zero coefficents must be given
    """
    degree = len(f)-1
    ans = 0
    for i in f:
        ans += i*x**degree
        degree -= 1
    return(ans)

def differentiate_polynomial(f):
    fdash = []
    degree = len(f)-1
    for i in f:
        fdash.append(i*degree)
        degree -=1                
    constant = fdash.pop()
    return fdash

def newton_raphson(f,x0,iterations):
    """
    Finds runs the set number of iterations to provide and estimate of the root 
    closest to x0:
        - f is a polynomial represented as a list of co efficents
        - x0 is the intial guess of the root
        - runs for the specified number of iterations
    implementation of the newton_raphson root fiding method
    """    
    current = x0
    fdash = differentiate_polynomial(f)
    print(fdash)
    for i in range(iterations):   
        current = current - evaluate_polynomial(f,current)/evaluate_polynomial(fdash,current)
    return current
        
        
qubic = [-2,-4,5,-6]        
newton_raphson(qubic,-4,1)

def euler_2(x0,f_of_x, fdash,step_size, step_number):
    """
    fdash is a tuple (a,b) where fdash =  (a*x - b*f(x))
    """
    for i in range(step_number):
        f_of_x += (fdash[0]*x0 + fdash[1]*f_of_x)*step_size
        x0 += step_size
    return f_of_x
    
x0 = 1
f_of_x = 2
step_size = 0.5
step_number = 4
fdash = (1.0,-1.0)

euler_2(x0,f_of_x, fdash,step_size, step_number)    
    
    
    
    
       