# -*- coding: utf-8 -*-
"""
two sum 

Created on Sun Sep 18 19:15:59 2016

@author: Lucy
"""

def two_sum(my_dict,my_list):
    count = 0
    for t in range(-10000,10000+1):
        for x in my_list:
            if t-x in my_dict and t-x != x:
                count = count + 1
                print(count, '  ',x,' + ',t-x,'=',t)
                break 
    return count

    
#open the file
my_file = open('2sum.txt')
my_dict = {}

i = 0 
for line in my_file: 
    i = i + 1
    x = int(line)
    my_dict[x] = 1
    #if i ==10 :
     #   break 
#print(my_dict)
my_list = list(my_dict.keys())

print(two_sum(my_dict,my_list))
