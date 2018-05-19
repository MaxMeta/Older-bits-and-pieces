# -*- coding: utf-8 -*-
"""
Created on Sat Mar  5 20:04:57 2016

@author: SpiffKringle
"""

def PassVsContinue(iterable,conditional,variant= "continue"):
    for i in iterable:
        if i == conditional:
            if variant == "continue":
                continue
            elif variant == "break":
                break
            elif variant == "pass":
                pass
            else:
                print "invalid fucntion value for variant"
                break
        print i,
        
        
PassVsContinue("the","h")
print
PassVsContinue("the","h","pass")
print
PassVsContinue("the","h","break")
print "***"
glo = 3

def ModifiesGlo(Val):
    global glo
    glo = Val


def ErrorGlo(Val,glo):
    global glo
    glo = Val
    
#SyntaxError: name 'glo' is local and global 
    
def DosentModifyGlo(Val):
    glo = Val

def TakesAGlobal(x,y):
    return x + y + glo
    
print TakesAGlobal(1,2)

DosentModifyGlo(100)

print

print TakesAGlobal(1,2)
    
ModifiesGlo(100)

print

print TakesAGlobal(1,2)


def NestedFunctions(x):
    def theNextLevel(y):
        return(y)
    z = x+3
    return theNextLevel(z)
    
    

    