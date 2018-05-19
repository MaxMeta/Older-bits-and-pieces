#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 20 10:21:08 2017

@author: spiffkringle
"""

import argparse, sys

parser=argparse.ArgumentParser()

parser.add_argument('--bar', '-b', help='Here you specify the value for argument bar, the default value is: bar_default')
parser.add_argument('--foo', '-f', help='Here you specify the value for argument foo, the default value is: foo_default')

args=parser.parse_args()

#print(args)
#print(sys)

foo = "foo_default" if not args.foo else args.foo 
bar = "bar_default" if not args.bar else args.bar 

print("the foo argument was: " + foo )
print("the bar argument was: " + bar)

#try calling this from the command line

"""
spiffkringle@sog-65bfyy1:~/Dropbox/Code/GNPS_UCSD$ python named_args.py -f chicken -b chips
the foo argument was: chicken
the bar argument was: chips

spiffkringle@sog-65bfyy1:~/Dropbox/Code/GNPS_UCSD$ python named_args.py --foo chicken --bar chips
the foo argument was: chicken
the bar argument was: chips

spiffkringle@sog-65bfyy1:~/Dropbox/Code/GNPS_UCSD$ python named_args.py --foo chicken 
the foo argument was: chicken
the bar argument was: bar_default

optional arguments:
  -h, --help         show this help message and exit
  --bar BAR, -b BAR  Here you specify the value for argument bar, the default
                     value is: bar_default
  --foo FOO, -f FOO  Here you specify the value for argument foo, the default
                     value is: foo_default

hopefully you get the idea!
"""

