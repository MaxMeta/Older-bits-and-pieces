#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 28 09:52:36 2017

@author: SpiffKringle
"""

def FizzBuzz():
    for i in range(100):
        p = i+1
        if p%3 == 0 and p%5 == 0: print("FizzBuzz")
        elif p%3 == 0: print("Fizz")
        elif p%5 ==0: print("Buzz")
        else: print(p)

def FizzBuzz2():
    for i in range(100):
        p = i+1
        if p%3 == 0:
            if not p%5 == 0:
                print("Fizz")
            else:
                print("FizzBuzz")
        elif p%5 == 0:
            print("Buzz")
        else:
            print(p)

def FizzBuzz3(p = 1,end = 100):
    if p == end:
        print("Buzz")
    else:
        if p%3 == 0 and p%5 == 0: print("FizzBuzz")
        elif p%3 == 0: print("Fizz")
        elif p%5 ==0: print("Buzz")
        else: print(p)
        FizzBuzz3(p+1)
    
def FizzBuzz4():
    for i in range(1,101):
        toPrint = ""
        if i%3 == 0: toPrint += "Fizz"
        if i%5 == 0: toPrint += "Buzz"
        if toPrint == "": toPrint = i
        print(toPrint)

def FizzBuzz5():
    """
    Unreadable but "clever"
    """
    print("\n".join([(i%3 == 2) * "Fizz" + (i%5 == 4)* "Buzz" or str(i+1) for i in range(100)]))
    #recall that an empty string is false in logicals
    #Could also use (i+1)%3 == 0, but more brackets are required
    #For any integer i that is dividable by n. i%(k*n-1) == n-1
    """
    True * "the"
    Out[140]: 'the'
    
    False * "the"
    Out[141]: ''
    
    0 or 10
    Out[139]: 10
    
    0 or "the"
    Out[143]: 'the'
    
    "" or "the"    
    InOut[144]: 'the'   
    
    "" or 10
    Out[145]: 10
    
    ...etc   
    """

def Silly():
    print("Blargy! Blargy! Blargy!")

[Silly() for _ in range(3)] # Convenstion dictates  _ for an unused variable, but could be any symbol.

[Silly() for i in range(3)]


        
        
        
            
    