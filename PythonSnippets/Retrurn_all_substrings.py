#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Jan  1 22:14:55 2017

@author: SpiffKringle
"""

def get_all_sublists(input_list):
  length = len(input_list)
  return [input_list[i:j+1] for i in xrange(length) for j in xrange(i,length)]

print get_all_sublists(['a','b','c'])