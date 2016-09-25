# -*- coding: utf-8 -*-
"""

Created on Sat Sep 24 19:33:07 2016

@author: Lucy
"""
import heapq


#open the file 
my_file = open('Median.txt')

my_list =[]

for x in my_file : 
    my_list.append(int(x))
    
print(my_list)
