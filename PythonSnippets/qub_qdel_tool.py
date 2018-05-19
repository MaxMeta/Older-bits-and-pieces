#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct  2 17:29:51 2017

@author: owenje
"""

with open('/Users/owenje/Desktop/ToQDel.txt', 'r') as F:
    for line in F:
        print("qdel " + line.split()[0])
        

for i in range(1,201):
    print("qsub antismash_NCBI.sh " + str("0"* (3 - len(str(i))) + str(i)))
    